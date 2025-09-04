import json
import datetime

def addToJSON(dicAdded): #Añade el diccionario obtenido a la lista.

    data = {}
    with open("tarea.json", "r", encoding="UTF-8") as f:
        content = f.read().strip()
        if content: 
            data = json.loads(content)
    
    idval = 0 if not data else max(int(k) for k in data.keys()) +1
    data[idval] = dicAdded

    with open("tarea.json", "w", encoding="UTF-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)    

def getFromJSON(): #Regresa un diccionario de todos los archivos dentro de las tareas.
    data = {}
    with open("tarea.json", "r", encoding="UTF-8") as f:
        content = f.read().strip()
        if content: 
            data = json.loads(content)
    return data