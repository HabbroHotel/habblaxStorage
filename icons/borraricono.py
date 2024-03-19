import os
from PIL import Image

# Ruta de los iconos
ruta_iconos = "/home/peyote/habb/icons"

# Obtener la lista de archivos en la ruta
archivos = os.listdir(ruta_iconos)

# Recorrer cada archivo y verificar si es una imagen válida
for archivo in archivos:
    # Verificar si el archivo es un PNG
    if archivo.lower().endswith(".png"):
        ruta_completa = os.path.join(ruta_iconos, archivo)
        try:
            # Intentar abrir el archivo como imagen
            img = Image.open(ruta_completa)
            img.verify()  # Verificar la integridad del archivo
        except (IOError, SyntaxError) as e:
            # Si ocurre un error al abrir o verificar la imagen, eliminar el archivo
            print(f"Archivo corrupto o inválido: {archivo}. Eliminando...")
            os.remove(ruta_completa)
        except Exception as e:
            print(f"Error desconocido al procesar {archivo}: {e}")
    else:
        # Si el archivo no es un PNG, ignorarlo
        print(f"Ignorando archivo no PNG: {archivo}")

print("Proceso completado.")
