#include <windows.h>
#include <shlobj.h>
#include <exdisp.h>
#include <shlwapi.h>
#include <vector>
#include <string>
#include <algorithm>
#include <iostream>
#include <cwctype>

// Link required Windows libraries automatically in Visual Studio
#pragma comment(lib, "ole32.lib")
#pragma comment(lib, "shlwapi.lib")

// Struct to track desktop items and their properties
struct DesktopItem {
    PITEMID_CHILD pidl;
    std::wstring parsingName;  // Real file name (with extension)
    std::wstring displayName;  // User-facing name (case-insensitive for sorting)
    std::wstring ext;          // File extension (lowercase)
    int category;              // 1: Recycle Bin, 2: Shortcuts, 3: Folders, 4: Files
};

// Helper function to fetch the Desktop's COM IFolderView interface
HRESULT GetDesktopFolderView(IFolderView** ppFV) {
    IShellWindows* pSW = NULL;
    HRESULT hr = CoCreateInstance(CLSID_ShellWindows, NULL, CLSCTX_LOCAL_SERVER, IID_PPV_ARGS(&pSW));
    if (FAILED(hr)) return hr;

    long lHwnd;
    IDispatch* pDisp = NULL;
    VARIANT vEmpty = { 0 };

    // Locate the specific Shell Window mapped to the Desktop
    hr = pSW->FindWindowSW(&vEmpty, &vEmpty, SWC_DESKTOP, &lHwnd, SWFO_NEEDDISPATCH, &pDisp);
    pSW->Release();
    if (FAILED(hr) || hr == S_FALSE) return E_FAIL;

    IShellBrowser* pSB = NULL;
    hr = IUnknown_QueryService(pDisp, SID_STopLevelBrowser, IID_PPV_ARGS(&pSB));
    pDisp->Release();
    if (FAILED(hr)) return hr;

    IShellView* pSV = NULL;
    hr = pSB->QueryActiveShellView(&pSV);
    pSB->Release();
    if (FAILED(hr)) return hr;

    hr = pSV->QueryInterface(IID_PPV_ARGS(ppFV));
    pSV->Release();
    return hr;
}

int main() {
    // Initialize COM Library
    HRESULT hr = CoInitializeEx(NULL, COINIT_APARTMENTTHREADED);
    if (FAILED(hr)) {
        std::wcerr << L"Failed to initialize COM library." << std::endl;
        return 1;
    }

    IFolderView* pFV = NULL;
    if (FAILED(GetDesktopFolderView(&pFV))) {
        std::wcerr << L"Failed to hook into Windows Desktop View. Make sure Explorer is running." << std::endl;
        CoUninitialize();
        return 1;
    }

    // Safely disable Auto-Arrange if it's turned on, otherwise positioning fails
    IFolderView2* pFV2 = NULL;
    if (SUCCEEDED(pFV->QueryInterface(IID_PPV_ARGS(&pFV2)))) {
        DWORD dwFlags = 0;
        if (SUCCEEDED(pFV2->GetCurrentFolderFlags(&dwFlags)) && (dwFlags & FWF_AUTOARRANGE)) {
            std::wcout << L"Disabling Desktop Auto-Arrange to apply custom layout..." << std::endl;
            pFV2->SetCurrentFolderFlags(FWF_AUTOARRANGE, 0);
        }
        pFV2->Release();
    }

    IShellFolder* pDesktopFolder = NULL;
    SHGetDesktopFolder(&pDesktopFolder);

    int itemCount = 0;
    pFV->ItemCount(SVGIO_ALLVIEW, &itemCount);

    std::vector<DesktopItem> items;

    // Enumerate through every item on the desktop
    for (int i = 0; i < itemCount; ++i) {
        PITEMID_CHILD pidl = NULL;
        if (SUCCEEDED(pFV->Item(i, &pidl))) {
            DesktopItem item;
            item.pidl = pidl;

            // 1. Get real file/parsing name (includes file extension)
            STRRET strretParse;
            if (SUCCEEDED(pDesktopFolder->GetDisplayNameOf(pidl, SIGDN_PARENTRELATIVEPARSING, &strretParse))) {
                wchar_t* pszName = NULL;
                StrRetToStrW(&strretParse, pidl, &pszName);
                if (pszName) {
                    item.parsingName = pszName;
                    CoTaskMemFree(pszName);
                }
            }

            // 2. Get normal display name (what the user actually sees)
            STRRET strretDisplay;
            if (SUCCEEDED(pDesktopFolder->GetDisplayNameOf(pidl, SIGDN_NORMALDISPLAY, &strretDisplay))) {
                wchar_t* pszName = NULL;
                StrRetToStrW(&strretDisplay, pidl, &pszName);
                if (pszName) {
                    item.displayName = pszName;
                    CoTaskMemFree(pszName);
                }
            }

            // Process lowercase extensions for case-insensitive grouping
            size_t dot = item.parsingName.find_last_of(L'.');
            if (dot != std::wstring::npos) {
                item.ext = item.parsingName.substr(dot);
                std::transform(item.ext.begin(), item.ext.end(), item.ext.begin(), ::towlower);
            }

            // Get shell item system attributes
            ULONG attrs = SFGAO_FOLDER | SFGAO_LINK;
            pDesktopFolder->GetAttributesOf(1, (LPCITEMIDLIST*)&pidl, &attrs);

            // 3. Assign Custom sorting categories based on requirements
            if (item.parsingName.find(L"{645FF040-5081-101B-9F08-00AA002F954E}") != std::wstring::npos) {
                item.category = 1; // Recycle Bin
            }
            else if ((attrs & SFGAO_LINK) || item.ext == L".lnk" || item.ext == L".url") {
                item.category = 2; // Icons & Shortcuts
            }
            else if (attrs & SFGAO_FOLDER) {
                item.category = 3; // Folders
            }
            else {
                item.category = 4; // Files
            }

            items.push_back(item);
        }
    }

    // Custom Comparator Logic
    std::sort(items.begin(), items.end(), [](const DesktopItem& a, const DesktopItem& b) {
        if (a.category != b.category) {
            return a.category < b.category; // Sort primarily by category rules (1 to 4)
        }
        if (a.category == 4) {
            if (a.ext != b.ext) {
                return a.ext < b.ext;      // Files sub-sort: Step A -> Group by extension
            }
        }
        // Case-insensitive alphabetical tie-breaker sort
        std::wstring nameA = a.displayName;
        std::wstring nameB = b.displayName;
        std::transform(nameA.begin(), nameA.end(), nameA.begin(), ::towlower);
        std::transform(nameB.begin(), nameB.end(), nameB.begin(), ::towlower);
        return nameA < nameB;
        });

    // Get current Windows Grid metrics for icon placement layout
    int iconSpacingX = GetSystemMetrics(SM_CXICONSPACING);
    int iconSpacingY = GetSystemMetrics(SM_CYICONSPACING);
    if (iconSpacingX <= 0) iconSpacingX = 100;
    if (iconSpacingY <= 0) iconSpacingY = 100;

    // Fetch the Main Display's working area
    RECT workArea;
    SystemParametersInfo(SPI_GETWORKAREA, 0, &workArea, 0);

    // FIX: Get the coordinates of the absolute top-left edge of your multi-monitor layout.
    // If your main display is on the right, virtualXOffset will be negative (e.g. -1920).
    int virtualXOffset = GetSystemMetrics(SM_XVIRTUALSCREEN);
    int virtualYOffset = GetSystemMetrics(SM_YVIRTUALSCREEN);

    // Subtracting a negative offset shifts our coordinates forward onto the main screen layout.
    int startX = workArea.left - virtualXOffset + 20;
    int startY = workArea.top - virtualYOffset + 20;

    int currentX = startX;
    int currentY = startY;
    int boundaryBottom = workArea.bottom - virtualYOffset;

    std::vector<LPCITEMIDLIST> pidlList;
    std::vector<POINT> pointList;

    // Build the layout structures sequentially in standard columns (Top-to-Bottom, Left-to-Right)
    for (const auto& item : items) {
        pidlList.push_back(item.pidl);
        POINT pt = { currentX, currentY };
        pointList.push_back(pt);

        currentY += iconSpacingY;
        // Wrap around to the next column if we reach the bottom of the main monitor workspace
        if (currentY + iconSpacingY > boundaryBottom) {
            currentY = startY;
            currentX += iconSpacingX;
        }
    }

    // Commit the calculated arrangements back to the Desktop Shell View
    std::wcout << L"Arranging " << items.size() << L" items on your main display..." << std::endl;
    pFV->SelectAndPositionItems((UINT)pidlList.size(), pidlList.data(), pointList.data(), SVSI_POSITIONITEM);

    // Memory clean up
    for (auto& item : items) {
        ILFree(item.pidl);
    }
    pDesktopFolder->Release();
    pFV->Release();
    CoUninitialize();

    std::wcout << L"Desktop icons sorted successfully on Main Display!" << std::endl;
    return 0;
}