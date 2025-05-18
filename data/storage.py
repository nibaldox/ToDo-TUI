"""
Módulo para la persistencia de tareas en archivo JSON.
Permite guardar y cargar la lista de tareas de FocusFlow.
"""
import json
from typing import List
RUTA_ARCHIVO = "data/tareas.json"

def guardar_tareas(tareas: list):
    """
    Guarda una lista de diccionarios de tareas en un archivo JSON.
    """
    with open(RUTA_ARCHIVO, "w", encoding="utf-8") as f:
        json.dump(tareas, f, ensure_ascii=False, indent=2)

def cargar_tareas() -> list:
    """
    Carga una lista de diccionarios de tareas desde un archivo JSON.
    Si el archivo no existe, retorna una lista vacía.
    """
    try:
        with open(RUTA_ARCHIVO, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
