import os
import json
import time
import requests

url_base = "https://habbox.fr/nitro/bundled/furniture/icons/"
extension = ".png"
wait_time = 0.5

def es_imagen_valida(respuesta):
    try:
        if not respuesta.headers.get('content-type').startswith('image'):
            return False  # La respuesta no es una imagen válida
        return True
    except Exception as e:
        print(f"Error al verificar la imagen: {e}")
        return False

with open("Data2.json", "r", encoding="utf-8") as f:
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
            if es_imagen_valida(response):
                with open(filename, "wb") as f:
                    f.write(response.content)
                print("Imagen descargada correctamente.")
            else:
                print("La respuesta no es una imagen válida.")
            time.sleep(wait_time)
