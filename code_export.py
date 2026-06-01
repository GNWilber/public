import os
from pathlib import Path

# ==================== WHITELISTA ROZSZERZEŃ ====================
# Tutaj możesz bardzo łatwo dodawać lub usuwać obsługiwane pliki.
# Pamiętaj, aby wpisywać je z kropką i małymi literami.
WHITELIST = {
    '.java', '.py', '.cpp', '.c', '.h', '.hpp', '.cs', '.js', '.ts', 
    '.html', '.css', '.rs', '.go', '.php', '.rb', '.kt', '.xml', '.swift', '.sh'
}
# ===============================================================

IGNORED_DIRS = {'.git', 'node_modules', '__pycache__', 'venv', '.idea', '.vscode'}
OUTPUT_FILE = "code.md"

def pobierz_liste_plikow(opcja, sciezka_skryptu, sciezka_wyjsciowa):
    aktualny_folder = Path.cwd()
    znalezione_pliki = []
    
    if opcja == '1':
        for element in aktualny_folder.iterdir():
            if element.is_file() and element.suffix.lower() in WHITELIST:
                if element.resolve() != sciezka_skryptu and element.resolve() != sciezka_wyjsciowa:
                    znalezione_pliki.append(element)
                    
    elif opcja == '2':
        for element in aktualny_folder.rglob('*'):
            if element.is_file() and element.suffix.lower() in WHITELIST:
                if not any(part in IGNORED_DIRS or part.startswith('.') for part in element.parts[:-1]):
                    if element.resolve() != sciezka_skryptu and element.resolve() != sciezka_wyjsciowa:
                        znalezione_pliki.append(element)
                        
    return sorted(znalezione_pliki)

def uruchom_eksport():
    print("========================================")
    print("   EKSPORTER KODU ŹRÓDŁOWEGO DO .MD   ")
    print("========================================")
    print("1. Przeszukaj TYLKO aktualny folder")
    print("2. Przeszukaj aktualny folder ORAZ wszystkie podfoldery")
    print("----------------------------------------")
    
    wybor = ""
    while wybor not in ['1', '2']:
        wybor = input("Wybierz opcję (1 lub 2): ").strip()
        
    sciezka_skryptu = Path(__file__).resolve()
    sciezka_wyjsciowa = Path(OUTPUT_FILE).resolve()
    
    pliki = pobierz_liste_plikow(wybor, sciezka_skryptu, sciezka_wyjsciowa)
    
    if not pliki:
        print("\nNie znaleziono żadnych plików spełniających kryteria.")
        return

    print(f"\nZnaleziono {len(pliki)} plików. Trwa zapisywanie do {OUTPUT_FILE}...")

    with open(OUTPUT_FILE, "w", encoding="utf-8") as plik_md:
        for sciezka_pliku in pliki:
            sciezka_wyswietlana = sciezka_pliku.relative_to(Path.cwd())
            jezyk_md = sciezka_pliku.suffix.lower().lstrip('.')
            
            try:
                with open(sciezka_pliku, "r", encoding="utf-8", errors="replace") as f_kod:
                    zawartosc = f_kod.read()

                plik_md.write(f"{sciezka_wyswietlana}:\n")
                plik_md.write(f"```{jezyk_md}\n")
                plik_md.write(zawartosc)
                
                if not zawartosc.endswith("\n"):
                    plik_md.write("\n")
                    
                plik_md.write("```\n\n")
                print(f" -> Dodano: {sciezka_wyswietlana}")

            except Exception as e:
                print(f" X Błąd podczas odczytu {sciezka_wyswietlana}: {e}")

    print(f"\nSukces! Cały kod został scalony w pliku: {OUTPUT_FILE}")

if __name__ == "__main__":
    uruchom_eksport()