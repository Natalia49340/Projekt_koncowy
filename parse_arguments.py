import argparse
from pathlib import Path
def parse_arguments():
    parser = argparse.ArgumentParser(description="Program do konwersji danych")
    parser.add_argument("input_file", type=str, help="nazwa pliku wejściowego")
    parser.add_argument("output_file", type=str, help="nazwa pliku wyjściowego")
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    try:
        args = parse_arguments()
        input_file = args.input_file
        output_file = args.output_file
        print("Przetwarzanie plików...")
        print("Plik wejściowy: ", input_file)
        print("Plik wyjściowy: ", output_file)

        file_path = Path(input_file)
        if not file_path.exists():
            raise ValueError("Podany plik nie istnieje.")
        elif not file_path.is_file():
            raise ValueError("Podana ścieżka nie wskazuje na plik.")

        file_extension = file_path.suffix.lower()
        valid_extensions = [".xml", ".json", ".yml", ".yaml"]
        if file_extension not in valid_extensions:
            raise ValueError("Nieprawidłowe rozszerzenie pliku. Oczekiwano .xml, .json, .yml lub .yaml")

    except FileNotFoundError as e:
        print("Podany plik nie istnieje. ", str(e))
    except ValueError as e:
        print("Nieprawidłowy format danych.", str(e))
    except Exception as e:
        print("Wystąpił nieoczekiwany błąd:", str(e))