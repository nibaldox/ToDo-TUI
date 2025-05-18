# 🚀 FocusFlow - Gestor de Tareas TUI

![FocusFlow Banner](https://img.shields.io/badge/TUI-FocusFlow-blue?style=for-the-badge)

> Un gestor de tareas moderno y minimalista para la terminal, rápido, persistente y con interfaz amigable.

---

## Tabla de Contenido
- [Descripción](#descripción)
- [Demo](#demo)
- [Requisitos](#requisitos)
- [Instalación](#instalación)
- [Uso](#uso)
- [Funcionalidades principales](#funcionalidades-principales)
- [Estructura del proyecto](#estructura-del-proyecto)
- [Contribuir](#contribuir)
- [Créditos](#créditos)
- [Licencia](#licencia)

---

## Descripción

FocusFlow es un gestor de tareas basado en interfaz de usuario de texto (TUI), diseñado para maximizar la productividad y la organización personal o profesional desde la terminal. Permite gestionar tareas de forma eficiente, con opciones de filtrado, ordenamiento y persistencia automática en disco.

## Demo

```text
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃            FocusFlow - Gestor de Tareas TUI         ┃
┣━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━━━━━┫
┃ #    ┃ Título   ┃ Prioridad ┃ Categoría ┃ Completada ┃
┣━━━━━━╋━━━━━━━━━━╋━━━━━━━━━━━╋━━━━━━━━━━━╋━━━━━━━━━━━━┫
┃ 1    ┃ Informe  ┃ Alta      ┃ Trabajo   ┃ ✅         ┃
┃ 2    ┃ Compra   ┃ Normal    ┃ Personal  ┃ ❌         ┃
┗━━━━━━┻━━━━━━━━━━┻━━━━━━━━━━━┻━━━━━━━━━━━┻━━━━━━━━━━━━┛

[1] Listar tareas  [2] Agregar tarea  [3] Eliminar tarea
[4] Marcar tarea   [5] Editar tarea   [6] Filtrar
[7] Ordenar        [8] Salir
```

---

## Requisitos

- Python 3.8+
- [Rich](https://github.com/Textualize/rich) (requerido)
- (Opcional) [Textual](https://github.com/Textualize/textual) para futuras mejoras gráficas

## Instalación

1. Clona el repositorio:

   ```bash
   git clone https://github.com/nibaldox/ToDo-TUI.git
   cd ToDo-TUI
   ```

2. Instala las dependencias:

   ```bash
   pip install rich
   # o si tienes requirements.txt
   # pip install -r requirements.txt
   ```

## Uso

Ejecuta el gestor desde la terminal:

```bash
python main.py
```

Las tareas se guardan y cargan automáticamente desde el archivo `data/tareas.json`. Puedes cerrar y volver a abrir la aplicación sin perder tus datos.

---

## Funcionalidades principales

- Añadir, listar, editar y eliminar tareas
- Marcar tareas como completadas o pendientes
- Asignar prioridades y categorías a cada tarea
- Filtrar tareas por estado, prioridad o categoría
- Ordenar tareas por prioridad, estado o título
- Guardado y carga automática de tareas (persistencia en JSON)
- Interfaz amigable y minimalista
- Código limpio y extensible

## Estructura del proyecto

```
ToDo-TUI/
├── main.py                  # Entrada principal
├── tasks/
│   └── task_manager.py      # Lógica y modelo de tareas
├── ui/
│   └── tui.py               # Interfaz TUI
├── data/
│   ├── storage.py           # Persistencia en JSON
│   └── tareas.json          # Archivo de datos (autogenerado)
├── README.md
├── .gitignore
├── plan_implementacion.md
└── Gestor-de-tareas-TUI.pdf # Documento de requisitos
```

## Contribuir

¡Las contribuciones son bienvenidas! Puedes abrir issues, enviar PRs o sugerir mejoras.

1. Haz un fork del repositorio.
2. Crea una rama para tu funcionalidad: `git checkout -b feature/nueva-funcionalidad`
3. Realiza tus cambios y documenta tu código.
4. Haz commit y push: `git commit -m "Agrega nueva funcionalidad" && git push origin feature/nueva-funcionalidad`
5. Abre un Pull Request.

## Créditos

Desarrollado por [@nibaldox](https://github.com/nibaldox) y colaboradores.

## Licencia

MIT

---

### Notas adicionales

- El código está documentado y sigue los principios de clean code.
- Para desarrolladores: puedes ampliar la app añadiendo nuevas funcionalidades en los módulos correspondientes.
- Si tienes dudas o sugerencias, consulta el archivo `plan_implementacion.md` para el seguimiento del proyecto.

> Para más detalles, consulta el archivo `plan_implementacion.md`.
