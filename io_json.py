import json

import datetime


def loadJSON() -> (
    dict
):  # Regresa un diccionario de todos los archivos dentro de las tareas.
    data = {}
    with open("tarea.json", "r", encoding="UTF-8") as f:
        content = f.read().strip()
        if content:
            data = json.loads(content)
    return data


def getArrayFromJSON() -> (
    list[dict]
):  
    data = loadJSON()
    return [{"id": int(task_id), **task} for task_id, task in data.items()]


def addToJSON(dicAdded):  
    data = loadJSON()

    idval = 0 if not data else int(next(reversed(data.keys()))) + 1
    data[idval] = dicAdded

    with open("tarea.json", "w", encoding="UTF-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def deleteFromJSON(idval):
    data = loadJSON()
    if str(idval) in data:
        del data[str(idval)]
        with open("tarea.json", "w", encoding="UTF-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        return True
    return False
