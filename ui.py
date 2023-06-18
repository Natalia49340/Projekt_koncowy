import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QFileDialog
from PyQt5.QtCore import Qt, QRunnable, QThreadPool, pyqtSlot
import json
import yaml
import xml.etree.ElementTree as ET

class Worker(QRunnable):
    def __init__(self, func, *args, **kwargs):
        super().__init__()
        self.func = func
        self.args = args
        self.kwargs = kwargs

    @pyqtSlot()
    def run(self):
        self.func(*self.args, **self.kwargs)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Program z interfejsem użytkownika")
        self.layout = QVBoxLayout()
        self.label = QLabel("Wczytane dane:")
        self.layout.addWidget(self.label)
        self.button_load = QPushButton("Wczytaj dane")
        self.button_load.clicked.connect(self.load_data)
        self.layout.addWidget(self.button_load)
        self.button_save = QPushButton("Zapisz dane")
        self.button_save.clicked.connect(self.save_data)
        self.layout.addWidget(self.button_save)
        self.central_widget = QWidget()
        self.central_widget.setLayout(self.layout)
        self.setCentralWidget(self.central_widget)

    def load_data(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Wybierz plik", "", "JSON Files (*.json);;YAML Files (*.yml *.yaml);;XML Files (*.xml)")
        if file_path:
            worker = Worker(self.read_data, file_path)
            QThreadPool.globalInstance().start(worker)

    def read_data(self, file_path):
        if file_path.endswith(".json"):
            data = self.load_json_data(file_path)
        elif file_path.endswith(".yml") or file_path.endswith(".yaml"):
            data = self.load_yaml_data(file_path)
        elif file_path.endswith(".xml"):
            data = self.load_xml_data(file_path)
        else:
            print("Nieobsługiwany format pliku.")
            return

        self.display_data(data)

    def load_json_data(self, file_path):
        with open(file_path, "r") as file:
            data = json.load(file)
            return data

    def load_yaml_data(self, file_path):
        with open(file_path, "r") as file:
            data = yaml.safe_load(file)
            return data

    def load_xml_data(self, file_path):
        tree = ET.parse(file_path)
        root = tree.getroot()
        return root

    def display_data(self, data):
        self.label.setText(f"Wczytane dane:\n{data}")

    def save_data(self):
        file_path, _ = QFileDialog.getSaveFileName(self, "Zapisz jako", "", "JSON Files (*.json);;YAML Files (*.yml);;XML Files (*.xml)")
        if file_path:
            worker = Worker(self.write_data, file_path)
            QThreadPool.globalInstance().start(worker)

    def write_data(self, file_path):
        data = self.label.text().split("\n")[-1]

        if file_path.endswith(".json"):
            self.save_json_data(data, file_path)
        elif file_path.endswith(".yml") or file_path.endswith(".yaml"):
            self.save_yaml_data(data, file_path)
        elif file_path.endswith(".xml"):
            self.save_xml_data(data, file_path)
        else:
            print("Nieobsługiwany format pliku.")

    def save_json_data(self, data, file_path):
        data_dict = {"Wczytane dane": data}
        with open(file_path, "w") as file:
            json.dump(data_dict, file)

    def save_yaml_data(self, data, file_path):
        data_dict = {"Wczytane dane": data}
        with open(file_path, "w") as file:
            yaml.dump(data_dict, file)

    def save_xml_data(self, data, file_path):
        root = ET.Element("root")
        element = ET.SubElement(root, "WczytaneDane")
        element.text = data
        tree = ET.ElementTree(root)
        tree.write(file_path, encoding="utf-8", xml_declaration=True)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
