# Gianluca Galanti 4C-IN
# Json manager class
import json
from datetime import datetime


class JsonManager(object):
    file_name = "dati.json"
    file = None
    data = {"date_time": datetime.now().strftime("%d/%m/%Y %H:%M:%S"), "temperature": [], "humidity": [], "heat_index": [], "light": []}

    def __init__(self):
        return

    def write_data(self, data):
        self.open_file("a")
        self.file.write("\n")
        json.dump(data, self.file)
        self.close()
        return

    def read_data(self):
        self.open_file("r")
        data = json.load(self.file)
        return data

    def open_file(self, mode):
        if self.file is not None:
            self.close()

        try:
            self.file = open(self.file_name, mode)
        except:
            print("Error while opening the file.\nClose the file before opening it")


    def remove_data_from_file(self):
        self.open_file("w")
