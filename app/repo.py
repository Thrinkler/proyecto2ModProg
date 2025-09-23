from typing import Optional
from .tarea import Tarea, TareaCreate
from . import io_json


def get_task(task_id: int) -> Optional[Tarea]:
    task_dict = io_json.get_task_dict(task_id)
    return Tarea.from_dict(task_dict) if task_dict else None


def get_task_list() -> list[Tarea]:
    return [Tarea.from_dict(d) for d in io_json.list_task_dicts()]


def add_task(tarea_in: TareaCreate) -> Tarea:
    rec = io_json.insert_task_dict(tarea_in.to_dict())
    return Tarea.from_dict(rec)


def find_tasks(search_term: str) -> list[Tarea]:
    query = search_term.lower()
    return [
        task
        for task in get_task_list()
        if query in task.titulo.lower() or query in task.descripcion.lower()
    ]


def delete_task(task_id: int) -> Optional[Tarea]:
    t = get_task(task_id)
    if t:
        io_json.delete_task(task_id)
    return t


def complete_task(task_id: int) -> Optional[Tarea]:
    task = get_task(task_id)
    if not task:
        return None
    task.complete()
    rec = io_json.upsert_task_dict(task.to_dict())  
    return Tarea.from_dict(rec)

def save_task():
    pass

