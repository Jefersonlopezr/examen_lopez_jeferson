import json
import os

def cargar_datos(nombre_archivo):
    if not os.path.exists(nombre_archivo):
        return []

    try:
        with open(nombre_archivo, "r", encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def guardar_datos(nombre_archivo, datos):
    with open(nombre_archivo, "w", encoding="utf-8") as file:
        json.dump(datos, file, indent=4, ensure_ascii=False)
