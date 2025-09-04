import datetime
import json
class Tarea:

    def __init__(self, idval:int, titulo:str, prioridad:int, fecha:str,descripcion:str,completada:bool):
        self.id = idval
        self.titulo = titulo
        self.prioridad=prioridad
        self.fecha = fecha
        self.descripcion = descripcion
        self.completada = completada

    def returnDic(self):
        return vars(self)

    def fromJson(self):
        pass
    def toJson(self):
        return json.dumps(self.returnDic(),ensure_ascii = False, indent=2)
    def saveToJson(self):
        with open("tarea.json", "a",encoding="UTF-8") as f:
            f.write(self.toJson())
            

    
