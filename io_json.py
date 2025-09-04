import json

import datetime

def loadJSON() -> dict: #Regresa un diccionario de todos los archivos dentro de las tareas.
    data = {}
    with open("tarea.json", "r", encoding="UTF-8") as f:
        content = f.read().strip()
        if content: 
            data = json.loads(content)
    return data

def getFromJSON(): #Regresa una lista con todos los diccionarios dentro de las tareas.
    data = loadJSON()
    return [
        {"id": int(task_id), **task}
        for task_id, task in data.items()
    ]

def addToJSON(dicAdded): #Añade el diccionario obtenido a la lista.
    data = loadJSON()
    
    idval = 0 if not data else int(next(reversed(data.keys()))) + 1
    data[idval] = dicAdded

    with open("tarea.json", "w", encoding="UTF-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)    



def findFromJSON(substr): # Regresa una lista con los diccionarios que coinciden con el substring
    data = getFromJSON()
    resultados = [
        task 
        for task in data
        if substr in task["titulo"] or substr in task["descripcion"]
    ]

    return resultados