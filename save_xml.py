import sys
import xml.etree.ElementTree as ET

def file_syntax(file_path):
    try:
        with open(file_path, "r") as file:
            ET.fromstring(file.read())
        return True
    except ET.ParseError:
        return False

# wczytywanie danych z pliku YAML
def load_xml_data(file_path):
    if not file_syntax(file_path):
        print("Niepoprawna składnia pliku XML:", file_path)
        return None
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()
        return root
    except FileNotFoundError:
        print("Podany plik nie istnieje")
    except ET.ParseError as e:
        print("Błąd wczytywania pliku XML:", file_path)
    except Exception as e:
        print("Wystąpił nieoczekiwany błąd:", file_path)
    return None

# zapis danych do pliku XML
def save_xml_data(data, file_path):
    try:
        tree = ET.ElementTree(data)
        tree.write(file_path, encoding="utf-8", xml_declaration=True)
        print(f"Pomyślnie zapisano dane XML do pliku: {file_path}")
    except Exception as e:
        print("Wystąpił błąd podczas zapisu danych do pliku:", file_path)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Podaj nazwę pliku wejściowego i wyjściowego jako argumenty")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    data = load_xml_data(input_file)

    if data:
        print("Wczytano dane z pliku XML:")
        print(data)
        save_xml_data(data, output_file)
        print(f"Pomyślnie zapisano dane XML do pliku {output_file}")