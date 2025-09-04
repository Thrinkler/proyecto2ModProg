import datetime
import io_json
import json
class Tarea:

    def __init__(self, titulo:str, prioridad:int, fecha:str,descripcion:str,completada:bool):
        self.titulo = titulo
        self.prioridad=prioridad
        self.fecha = fecha
        self.descripcion = descripcion
        self.completada = completada

    def dic(self):
        return vars(self)

    def fromJson(self):
        pass
    def toJson(self):
        return json.dumps(self.returnDic(),ensure_ascii = False, indent=2)
    def saveToJson(self):
        io_json.addToJSON(dic())
        
            
tar = Tarea("segunda tarea",1,str(datetime.datetime.today),"",False)

io_json.addToJSON(tar.dic())
    
