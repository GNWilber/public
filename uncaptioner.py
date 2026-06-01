import os
import re
import sys

def list_srt_files():
    """Zwraca listę plików .srt w aktualnym katalogu."""
    return [f for f in os.listdir('.') if f.lower().endswith('.srt') and not f.endswith('_uncapped.srt')]

def process_srt(filename, mode):
    """Przetwarza plik SRT usuwając wybrane nawiasy i poprawiając strukturę."""
    # Definicje regex dla zwykłych i pełnoekranowych (japońskich) nawiasów
    pattern_brackets = r'\[[^\]]*\]|［[^］]*］'  # [] oraz ［］
    pattern_parentheses = r'\([^)]*\)|（[^）]*）'  # () oraz （）

    if mode == 1:
        pattern = pattern_brackets
    elif mode == 2:
        pattern = pattern_parentheses
    else:
        pattern = f"{pattern_brackets}|{pattern_parentheses}"

    # Odczyt pliku z wymuszeniem kodowania UTF-8 (wsparcie dla japońskich znaków)
    with open(filename, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    # Normalizacja końców linii (Windows \r\n -> Linux \n)
    content = content.replace('\r\n', '\n')
    
    # Podział na bloki napisów (blok oddzielony jest podwójną nową linią)
    blocks = content.strip().split('\n\n')
    
    new_blocks = []
    total_removed = 0
    block_counter = 1

    for block in blocks:
        lines = block.split('\n')
        if len(lines) < 3:
            continue  # Pomija uszkodzone bloki

        sub_id = lines[0]
        timestamp = lines[1]
        text_lines = lines[2:]

        new_text_lines = []
        for line in text_lines:
            # Re.subn zwraca krotkę: (nowy_tekst, liczba_skasowanych_wzorców)
            cleaned_line, count = re.subn(pattern, '', line)
            total_removed += count
            
            # Czyszczenie zbędnych spacji na początku i końcu linii
            cleaned_line = cleaned_line.strip()
            
            # Jeśli po usunięciu nawiasu linia nie jest pusta, zachowujemy ją
            if cleaned_line:
                new_text_lines.append(cleaned_line)

        # Jeśli blok nadal zawiera jakikolwiek tekst, zapisujemy go z nowym indeksem
        if new_text_lines:
            new_block = f"{block_counter}\n{timestamp}\n" + "\n".join(new_text_lines)
            new_blocks.append(new_block)
            block_counter += 1

    # Generowanie nazwy pliku wyjściowego
    name_part, ext = os.path.splitext(filename)
    output_filename = f"{name_part}_uncapped{ext}"

    # Zapis nowego pliku
    with open(output_filename, 'w', encoding='utf-8') as f:
        f.write("\n\n".join(new_blocks) + "\n")

    return output_filename, total_removed

def main():
    print("=== UNCAPTIONER ===")
    srt_files = list_srt_files()

    if not srt_files:
        print("Nie znaleziono żadnych plików .srt w aktualnym folderze.")
        input("\nNaciśnij Enter, aby zamknąć...")
        sys.exit()

    print("\nDostępne pliki .srt:")
    for idx, file in enumerate(srt_files, 1):
        print(f"[{idx}] {file}")

    # Wybór pliku
    while True:
        try:
            file_choice = int(input("\nWybierz numer pliku do przetworzenia: "))
            if 1 <= file_choice <= len(srt_files):
                selected_file = srt_files[file_choice - 1]
                break
            else:
                print("Nieprawidłowy numer. Spróbuj ponownie.")
        except ValueError:
            print("Wprowadź poprawną liczbę.")

    # Wybór trybu usuwania
    print("\nCo chcesz usunąć?")
    print("[1] Tylko nawiasy kwadratowe [ ] oraz ［ ］")
    print("[2] Tylko nawiasy okrągłe ( ) oraz （ ）")
    print("[3] Oba rodzaje nawiasów")
    
    while True:
        try:
            mode_choice = int(input("\nWybierz opcję (1-3): "))
            if mode_choice in [1, 2, 3]:
                break
            else:
                print("Nieprawidłowa opcja. Wybierz 1, 2 lub 3.")
        except ValueError:
            print("Wprowadź poprawną liczbę.")

    # Przetwarzanie
    print(f"\nPrzetwarzanie pliku: {selected_file}...")
    output_file, removed_count = process_srt(selected_file, mode_choice)
    
    print("-" * 40)
    print(f"Sukces! Utworzono plik: {output_file}")
    print(f"Łącznie usunięto nawiasów: {removed_count}")
    print("-" * 40)
    
    input("\nNaciśnij Enter, aby zakończyć...")

if __name__ == "__main__":
    main()