import os
from pathlib import Path

# ==================== WHITELISTA ROZSZERZEŃ ====================
# Tutaj możesz bardzo łatwo dodawać lub usuwać obsługiwane pliki.
# Pamiętaj, aby wpisywać je z kropką i małymi literami.
WHITELIST = {
    '.java', '.py', '.cpp', '.c', '.h', '.hpp', '.cs', '.js', '.ts', 
    '.html', '.css', '.rs', '.go', '.php', '.rb', '.kt', '.swift', '.sh'
}

# Foldery, które skrypt ma całkowicie POMIJAĆ przy głębokim przeszukiwaniu (opcja 2).
# Zapobiega to wklejaniu tysięcy linii kodu z bibliotek zewnętrznych.
IGNORED_DIRS = {'.git', 'node_modules', '__pycache__', 'venv', '.idea', '.vscode'}
# ===============================================================

def pobierz_liste_plikow(opcja):
    aktualny_folder = Path.cwd()
    znalezione_pliki = []
    
    if opcja == '1':
        # Opcja 1: Tylko aktualny folder (płaskie przeszukiwanie)
        for element in aktualny_folder.iterdir():
            if element.is_file() and element.suffix.lower() in WHITELIST:
                znalezione_pliki.append(element)
                
    elif opcja == '2':
        # Opcja 2: Aktualny folder oraz wszystkie podfoldery (rekurencyjnie)
        for element in aktualny_folder.rglob('*'):
            if element.is_file() and element.suffix.lower() in WHITELIST:
                # Sprawdź, czy jakikolwiek folder nadrzędny nie jest na liście ignorowanych
                # lub czy nie zaczyna się od kropki (foldery ukryte)
                if not any(part in IGNORED_DIRS or part.startswith('.') for part in element.parts[:-1]):
                    znalezione_pliki.append(element)
                    
    return sorted(znalezione_pliki)

def uruchom_eksport(nazwa_wyjsciowa="code.md"):
    print("========================================")
    print("   EKSPORTER KODU ŹRÓDŁOWEGO DO .MD   ")
    print("========================================")
    print("1. Przeszukaj TYLKO aktualny folder")
    print("2. Przeszukaj aktualny folder ORAZ wszystkie podfoldery")
    print("----------------------------------------")
    
    wybor = ""
    while wybor not in ['1', '2']:
        wybor = input("Wybierz opcję (1 lub 2): ").strip()
    
    pliki = pobierz_liste_plikow(wybor)
    
    if not pliki:
        print("\nNie znaleziono żadnych plików spełniających kryteria whitelisty.")
        return

    print(f"\nZnaleziono {len(pliki)} plików. Trwa zapisywanie do {nazwa_wyjsciowa}...")

    # Zapis do pliku code.md z wymuszonym kodowaniem UTF-8 (działa tak samo na Windows/Linux)
    with open(nazwa_wyjsciowa, "w", encoding="utf-8") as plik_md:
        for sciezka_pliku in pliki:
            # Pobieramy ścieżkę relatywną (np. "src/Main.java" zamiast pełnej ścieżki dyskowej)
            sciezka_wyswietlana = sciezka_pliku.relative_to(Path.cwd())
            
            # Dynamiczne mapowanie rozszerzenia na język markdown (np. .py -> ```python)
            jezyk_md = sciezka_pliku.suffix.lower().lstrip('.')
            
            try:
                with open(sciezka_pliku, "r", encoding="utf-8", errors="replace") as f_kod:
                    zawartosc = f_kod.read()

                # Formatowanie Markdown zgodne z Twoim życzeniem
                plik_md.write(f"{sciezka_wyswietlana}:\n")
                plik_md.write(f"```{jezyk_md}\n")
                plik_md.write(zawartosc)
                
                # Zabezpieczenie przed brakiem nowej linii na końcu oryginalnego pliku
                if not zawartosc.endswith("\n"):
                    plik_md.write("\n")
                    
                plik_md.write("```\n\n")
                print(f" -> Dodano: {sciezka_wyswietlana}")

            except Exception as e:
                print(f" X Błąd podczas odczytu pliku {sciezka_wyswietlana}: {e}")

    print(f"\nSukces! Cały kod został scalony w pliku: {nazwa_wyjsciowa}")

if __name__ == "__main__":
    uruchom_eksport()