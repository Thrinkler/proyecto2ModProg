import json
import datetime

def getFromJSON(): #Regresa un diccionario de todos los archivos dentro de las tareas.
    data = {}
    with open("tarea.json", "r", encoding="UTF-8") as f:
        content = f.read().strip()
        if content: 
            data = json.loads(content)
    return data

def addToJSON(dicAdded): #Añade el diccionario obtenido a la lista.
    data = getFromJSON()
    idval = 0 if not data else max(int(k) for k in data.keys()) +1
    data[idval] = dicAdded

    with open("tarea.json", "w", encoding="UTF-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)    



def findFromJSON(substr): # Regresa una lista con los diccionarios que coinciden con el substring
    data = getFromJSON()
    resultados = []
    for dat in data:
        if(substr in data[dat]["titulo"] or substr in data[dat]["descripcion"]):
            resultados.append(data[dat])
    return resultados