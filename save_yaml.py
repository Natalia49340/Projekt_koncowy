import sys
import yaml

def file_syntax(yaml_str):
     try:
         yaml.safe_load(yaml_str)
         return True
     except yaml.YAMLError:
         return False

# wczytywanie danych z pliku YAML
def load_yaml_data(file_path):
     with open(file_path, "r") as file:
         yaml_content = file.read()
         if not file_syntax(yaml_content):
             print("Niepoprawna składnia pliku YAML:", file_path)
             return None
         try:
             data = yaml.safe_load(yaml_content)
             return data
         except FileNotFoundError:
             print("Podany plik nie istnieje")
         except yaml.YAMLError as e:
             print("Błąd wczytywania danych YAML:", file_path)
         except Exception as e:
             print("Wystąpił nieoczekiwany błąd:", file_path)
         return None

#zapis danych do pliku YAML
def save_yaml_data(data,file_path):
    with open(file_path,"w") as file:
        try:
            yaml.dump(data,file)
            print("Pomyślnie zapisano dane YAML do pliku:", file_path)
        except Exception as e:
            print("Wystąpił błąd podczas zapisu danych YAML:", file_path)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Podaj nazwy plików wejściowego i wyjściowego jako argumenty.")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    data = load_yaml_data(input_file)

    if data:
        print("Wczytano dane z pliku YAML:")
        print(data)
        save_yaml_data(data, output_file)
        print(f"Pomyślnie zapisano dane YAML do pliku {output_file}")
