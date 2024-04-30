# Gianluca Galanti 4C-IN
# Json manager class
import json
from datetime import datetime


class JsonManager(object):
    file_name = "dati.json"
    file = None
    data = {"device_id": "", "date_time": datetime.now().strftime("%d/%m/%Y %H:%M:%S"), "temperature": [], "humidity": [], "heat_index": [], "light": []}

    def __init__(self):
        return

    def write_data(self, data):
        self.open_file("a")
        self.file.write("\n")

        for i in range(data["temperature"].lenght):
            self.data["temperature"].extend(data["temperature"][i])
            self.data["humidity"].extend(data["humidity"][i])
            self.data["heat_index"].extend(data["heat_index"][i])
            self.data["light"].extend(data["light"][i])

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


    def close(self):
        self.file.close()
        self.file = None
        return
