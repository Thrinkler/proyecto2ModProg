from tarea import Tarea
import io_json

def get_task(id: int) -> Tarea:
    io_json.get_task_dict_from_json(id)
    task = Tarea.from_dict(task) if task else None
    return task

def get_task_list() -> list[Tarea]:
    task_dictionary = io_json.get_array_from_json()
    return [Tarea.from_dict(task) for task in task_dictionary]

def add_task(tarea: Tarea) -> Tarea:
    io_json.add_to_json(tarea.dic())
    return tarea

def find_tasks(search_term: str) -> list[Tarea]:
    all_tasks = get_task_list()
    
    matching_tasks = [task for task in all_tasks if search_term.lower() in task.titulo.lower() or search_term.lower() in task.descripcion.lower()]
    return matching_tasks

def delete_task(id: int) -> Tarea:
    task = get_task(id)
    io_json.delete_task_from_json(id)
    return task

def save_task():
    pass

def complete_task(id: int) -> Tarea:
    task = get_task(id)
    if task:
        task.complete()
        io_json.add_to_json(task.dic())
    return task
