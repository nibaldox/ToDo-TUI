"""
Módulo de la interfaz TUI para FocusFlow.
Contiene la función principal para iniciar la interfaz de usuario.
"""

from rich.console import Console
from rich.table import Table
from tasks.task_manager import Task, TaskManager

console = Console()

def mostrar_menu():
    """
    Muestra el menú principal de la aplicación.
    """
    console.print("\n[bold cyan]FocusFlow - Gestor de Tareas TUI[/bold cyan]", justify="center")
    console.print("[1] Listar tareas")
    console.print("[2] Agregar tarea")
    console.print("[3] Eliminar tarea")
    console.print("[4] Marcar tarea como completada/pendiente")
    console.print("[5] Editar tarea")
    console.print("[6] Filtrar tareas")
    console.print("[7] Ordenar tareas")
    console.print("[8] Salir")

def mostrar_tareas(task_manager: TaskManager, tareas=None):
    """
    Muestra la lista de tareas en formato de tabla.
    Si se pasa una lista de tareas, muestra solo esas; si no, muestra todas.
    """
    if tareas is None:
        tareas = task_manager.listar_tareas()
    if not tareas:
        console.print("[yellow]No hay tareas registradas.[/yellow]")
        return
    tabla = Table(title="Tareas")
    tabla.add_column("#", style="dim", width=4)
    tabla.add_column("Título", style="bold")
    tabla.add_column("Prioridad")
    tabla.add_column("Categoría")
    tabla.add_column("Completada")
    for idx, tarea in enumerate(tareas, 1):
        tabla.add_row(
            str(idx),
            tarea.titulo,
            tarea.prioridad,
            tarea.categoria,
            "✅" if tarea.completada else "❌"
        )
    console.print(tabla)

def agregar_tarea(task_manager: TaskManager):
    """
    Solicita los datos de una nueva tarea y la agrega al gestor.
    """
    titulo = console.input("[bold green]Título de la tarea:[/bold green] ")
    descripcion = console.input("Descripción (opcional): ")
    prioridad = console.input("Prioridad [Baja/Normal/Alta] (por defecto 'Normal'): ") or "Normal"
    categoria = console.input("Categoría (por defecto 'General'): ") or "General"
    tarea = Task(titulo, descripcion, prioridad, categoria)
    task_manager.agregar_tarea(tarea)
    console.print("[green]Tarea agregada exitosamente.[/green]")

def eliminar_tarea(task_manager: TaskManager):
    """
    Permite eliminar una tarea seleccionando su número en la lista y guarda los cambios.
    """
    mostrar_tareas(task_manager)
    if not task_manager.tareas:
        return
    try:
        idx = int(console.input("[red]Número de tarea a eliminar:[/red] ")) - 1
        if 0 <= idx < len(task_manager.tareas):
            tarea_eliminada = task_manager.tareas[idx]
            task_manager.eliminar_tarea(idx)
            console.print(f"[green]Tarea '{tarea_eliminada.titulo}' eliminada correctamente.[/green]")
        else:
            console.print("[red]Índice fuera de rango.[/red]")
    except ValueError:
        console.print("[red]Entrada inválida. Debe ser un número.[/red]")

def marcar_tarea(task_manager: TaskManager):
    """
    Permite marcar una tarea como completada o pendiente y guarda los cambios.
    """
    mostrar_tareas(task_manager)
    if not task_manager.tareas:
        return
    try:
        idx = int(console.input("[yellow]Número de tarea a marcar:[/yellow] ")) - 1
        if 0 <= idx < len(task_manager.tareas):
            tarea = task_manager.tareas[idx]
            task_manager.marcar_tarea(idx)
            estado = "completada" if not tarea.completada else "pendiente"
            # El estado se invierte porque ya fue cambiado en el método
            console.print(f"[cyan]Tarea '{tarea.titulo}' marcada como {estado}.[/cyan]")
        else:
            console.print("[red]Índice fuera de rango.[/red]")
    except ValueError:
        console.print("[red]Entrada inválida. Debe ser un número.[/red]")

def editar_tarea(task_manager: TaskManager):
    """
    Permite editar los campos de una tarea seleccionada y guarda los cambios.
    """
    mostrar_tareas(task_manager)
    if not task_manager.tareas:
        return
    try:
        idx = int(console.input("[blue]Número de tarea a editar:[/blue] ")) - 1
        if 0 <= idx < len(task_manager.tareas):
            tarea = task_manager.tareas[idx]
            nuevo_titulo = console.input(f"Nuevo título (actual: {tarea.titulo}): ") or tarea.titulo
            nueva_descripcion = console.input(f"Nueva descripción (actual: {tarea.descripcion}): ") or tarea.descripcion
            nueva_prioridad = console.input(f"Nueva prioridad [Baja/Normal/Alta] (actual: {tarea.prioridad}): ") or tarea.prioridad
            nueva_categoria = console.input(f"Nueva categoría (actual: {tarea.categoria}): ") or tarea.categoria
            task_manager.editar_tarea(idx, nuevo_titulo, nueva_descripcion, nueva_prioridad, nueva_categoria)
            console.print(f"[green]Tarea '{nuevo_titulo}' editada correctamente.[/green]")
        else:
            console.print("[red]Índice fuera de rango.[/red]")
    except ValueError:
        console.print("[red]Entrada inválida. Debe ser un número.[/red]")

def filtrar_tareas(task_manager: TaskManager):
    """
    Permite filtrar tareas por estado, prioridad o categoría.
    """
    console.print("\n[bold]Opciones de filtro:[/bold]")
    console.print("[1] Estado (completadas/pendientes)")
    console.print("[2] Prioridad")
    console.print("[3] Categoría")
    opcion = console.input("Selecciona filtro: ")
    tareas = task_manager.listar_tareas()
    if opcion == "1":
        estado = console.input("[cyan]Mostrar solo [completadas/pendientes]: [/cyan]").strip().lower()
        if estado == "completadas":
            filtradas = [t for t in tareas if t.completada]
        elif estado == "pendientes":
            filtradas = [t for t in tareas if not t.completada]
        else:
            console.print("[red]Opción de estado inválida.[/red]")
            return
        mostrar_tareas(task_manager, filtradas)
    elif opcion == "2":
        prioridad = console.input("[cyan]Prioridad a mostrar [Baja/Normal/Alta]: [/cyan]").strip().capitalize()
        filtradas = [t for t in tareas if t.prioridad.lower() == prioridad.lower()]
        mostrar_tareas(task_manager, filtradas)
    elif opcion == "3":
        categoria = console.input("[cyan]Categoría a mostrar: [/cyan]").strip()
        filtradas = [t for t in tareas if t.categoria.lower() == categoria.lower()]
        mostrar_tareas(task_manager, filtradas)
    else:
        console.print("[red]Opción de filtro no válida.[/red]")

def ordenar_tareas(task_manager: TaskManager):
    """
    Permite ordenar tareas por prioridad, estado o título.
    """
    console.print("\n[bold]Opciones de ordenamiento:[/bold]")
    console.print("[1] Prioridad")
    console.print("[2] Estado (completadas primero)")
    console.print("[3] Título (A-Z)")
    opcion = console.input("Selecciona orden: ")
    tareas = task_manager.listar_tareas().copy()
    if opcion == "1":
        prioridad_orden = {"Alta": 0, "Normal": 1, "Baja": 2}
        tareas.sort(key=lambda t: prioridad_orden.get(t.prioridad.capitalize(), 3))
    elif opcion == "2":
        tareas.sort(key=lambda t: not t.completada)
    elif opcion == "3":
        tareas.sort(key=lambda t: t.titulo.lower())
    else:
        console.print("[red]Opción de ordenamiento no válida.[/red]")
        return
    mostrar_tareas(task_manager, tareas)

def iniciar_tui():
    """
    Inicia la interfaz TUI del gestor de tareas.
    """
    task_manager = TaskManager()
    while True:
        mostrar_menu()
        opcion = console.input("\n[bold cyan]Selecciona una opción:[/bold cyan] ")
        if opcion == "1":
            mostrar_tareas(task_manager)
        elif opcion == "2":
            agregar_tarea(task_manager)
        elif opcion == "3":
            eliminar_tarea(task_manager)
        elif opcion == "4":
            marcar_tarea(task_manager)
        elif opcion == "5":
            editar_tarea(task_manager)
        elif opcion == "6":
            filtrar_tareas(task_manager)
        elif opcion == "7":
            ordenar_tareas(task_manager)
        elif opcion == "8":
            console.print("[bold magenta]¡Hasta luego![/bold magenta]")
            break
        else:
            console.print("[red]Opción no válida. Intenta de nuevo.[/red]")
