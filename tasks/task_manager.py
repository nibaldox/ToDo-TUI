"""
Módulo principal para la gestión de tareas en FocusFlow.
Contiene la clase TaskManager y la definición de la estructura de una tarea.
"""

from typing import List
from data.storage import guardar_tareas, cargar_tareas

class Task:
    """
    Clase que representa una tarea.
    """
    def __init__(self, titulo: str, descripcion: str = "", prioridad: str = "Normal", categoria: str = "General", completada: bool = False):
        self.titulo = titulo
        self.descripcion = descripcion
        self.prioridad = prioridad
        self.categoria = categoria
        self.completada = completada

    def to_dict(self):
        """
        Convierte la tarea a un diccionario serializable.
        """
        return {
            "titulo": self.titulo,
            "descripcion": self.descripcion,
            "prioridad": self.prioridad,
            "categoria": self.categoria,
            "completada": self.completada,
        }

class TaskManager:
    """
    Clase para gestionar el CRUD de tareas con persistencia automática.
    """
    def __init__(self):
        # Carga los datos como diccionarios y los convierte a objetos Task
        self.tareas: List[Task] = [Task(**td) for td in cargar_tareas()]

    def _guardar(self):
        """
        Guarda la lista de tareas como lista de diccionarios.
        """
        guardar_tareas([t.to_dict() for t in self.tareas])

    def agregar_tarea(self, tarea: Task):
        """Agrega una nueva tarea a la lista y guarda los cambios."""
        self.tareas.append(tarea)
        self._guardar()

    def listar_tareas(self) -> List[Task]:
        """Devuelve la lista de tareas."""
        return self.tareas

    def eliminar_tarea(self, idx: int):
        """Elimina una tarea por índice y guarda los cambios."""
        if 0 <= idx < len(self.tareas):
            self.tareas.pop(idx)
            self._guardar()

    def editar_tarea(self, idx: int, titulo: str, descripcion: str, prioridad: str, categoria: str):
        """Edita los campos de una tarea y guarda los cambios."""
        if 0 <= idx < len(self.tareas):
            tarea = self.tareas[idx]
            tarea.titulo = titulo
            tarea.descripcion = descripcion
            tarea.prioridad = prioridad
            tarea.categoria = categoria
            self._guardar()

    def marcar_tarea(self, idx: int):
        """Alterna el estado completada de una tarea y guarda los cambios."""
        if 0 <= idx < len(self.tareas):
            tarea = self.tareas[idx]
            tarea.completada = not tarea.completada
            self._guardar()
