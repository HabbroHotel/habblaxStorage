import requests
import os
import json
import time

url_base = "https://swfs.kubbo.city/dcr/hof_furni/icons"
extension = ".png"
wait_time = 0.5

with open("FurnitureData.json", "r", encoding="utf-8") as f:
    data = json.load(f)


    for items in data["roomitemtypes"]["furnitype"]:
        classname = items["classname"]
        filename = classname.replace("*", "-") + "_icon" + extension
        if os.path.exists(filename):
            print("El archivo ya existe:", classname)
        else:
            url = url_base + "/" + classname + "_icon" + extension
            print("Descargando imagen de la clase:", classname)
            response = requests.get(url)
            with open(filename, "wb") as f:
                f.write(response.content)
            time.sleep(wait_time)
