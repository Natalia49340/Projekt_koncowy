import yaml

def file_syntax(yaml_str):
    try:
        yaml.safe_load(yaml_str)
        return True
    except yaml.YAMLError:
        return False

 #wczytywanie danych z pliku YAML
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

input_file = input("Podaj nazwę pliku: ")
data = load_yaml_data(input_file)

if data:
    print("Wczytano dane z pliku YAML:")
    print(data)

 #zapis danych do pliku YAML
def save_yaml_data(data,file_path):
    with open(file_path,"w") as file:
        try:
            yaml.dump(data,file)
            print("Pomyślnie zapisano dane YAML do pliku:", file_path)
        except Exception as e:
            print("Wystąpił błąd podczas zapisu danych YAML:", file_path)

output_file = input("Podaj nazwę pliku do zapisu: ")
save_yaml_data(data,output_file)