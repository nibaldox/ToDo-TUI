# FocusFlow - Gestor de Tareas TUI

## Descripción

FocusFlow es un gestor de tareas basado en interfaz de usuario de texto (TUI), diseñado para maximizar la productividad y la organización personal o profesional desde la terminal. Permite gestionar tareas de forma eficiente, con opciones de filtrado, ordenamiento y persistencia automática en disco.

## Requisitos

- Python 3.8+
- [Rich](https://github.com/Textualize/rich) (requerido)
- (Opcional) [Textual](https://github.com/Textualize/textual) para futuras mejoras gráficas

## Instalación

1. Clona el repositorio:

   ```bash
   git clone <URL_DEL_REPOSITORIO>
   ```

2. Instala las dependencias:

   ```bash
   pip install rich
   ```

## Uso

Ejecuta el gestor desde la terminal:

```bash
python main.py
```

Las tareas se guardan y cargan automáticamente desde el archivo `data/tareas.json`. Puedes cerrar y volver a abrir la aplicación sin perder tus datos.

## Funcionalidades principales

- Añadir, listar, editar y eliminar tareas
- Marcar tareas como completadas o pendientes
- Asignar prioridades y categorías a cada tarea
- Filtrar tareas por estado, prioridad o categoría
- Ordenar tareas por prioridad, estado o título
- Guardado y carga automática de tareas (persistencia en JSON)

## Estructura del proyecto

- `main.py`: Entrada principal de la aplicación
- `tasks/task_manager.py`: Lógica y modelo de las tareas, gestión CRUD y persistencia
- `ui/tui.py`: Interfaz de usuario TUI, menú y comandos
- `data/storage.py`: Módulo de persistencia en JSON
- `data/tareas.json`: Archivo de almacenamiento de tareas (se crea automáticamente)
- `README.md`, `.gitignore`, `plan_implementacion.md`: Documentación y control

## Licencia

MIT

---

### Notas adicionales
- El código está documentado y sigue los principios de clean code.
- Para desarrolladores: puedes ampliar la app añadiendo nuevas funcionalidades en los módulos correspondientes.
- Si tienes dudas o sugerencias, consulta el archivo `plan_implementacion.md` para el seguimiento del proyecto.

---

> Para más detalles, consulta el archivo `plan_implementacion.md`.
