import sys
import xml.etree.ElementTree as ET
def file_syntax(file_path):
    try:
        with open(file_path, "r") as file:
            ET.fromstring(file.read())
        return True
    except ET.ParseError:
        return False

# wczytywanie danych z pliku XML
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

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Podaj nazwę pliku wejściowego i wyjściowego jako argumenty")
        sys.exit(1)

    input_file = sys.argv[1]

    data = load_xml_data(input_file)

    if data:
        print("Wczytano dane z pliku XML:")
        print(data)