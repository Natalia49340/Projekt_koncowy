import sys
import json

def file_syntax(json_str):
    try:
        json.loads(json_str)
        return True
    except ValueError:
        return False

# wczytywanie danych z pliku .json
def load_json_data(file_path):
    with open(file_path, "r") as file:
        json_content = file.read()
        if not file_syntax(json_content):
            print("Niepoprawna składnia pliku JSON:", file_path)
            return None
        try:
            data = json.loads(json_content)
            return data
        except FileNotFoundError:
            print("Podany plik nie istnieje")
        except json.JSONDecodeError as e:
            print("Błąd wczytywania danych JSON:", file_path)
        except Exception as e:
            print("Wystąpił nieoczekiwany błąd:", file_path)
        return None

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Podaj nazwę pliku wejściowego i wyjściowego jako argumenty.")
        sys.exit(1)

    input_file = sys.argv[1]

    data = load_json_data(input_file)

    if data:
        print("Wczytano dane z pliku JSON:")
        print(data)
