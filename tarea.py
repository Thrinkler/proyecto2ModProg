import datetime
import io_json
import json
class Tarea:

    @staticmethod
    def returnAll():
        return io_json.getFromJSON()
    
    @staticmethod
    def locate(substr):
        return io_json.findFromJSON(substr)

    def __init__(self, dictionary: dict):
        self.titulo = dictionary["titulo"]
        self.prioridad=dictionary["prioridad"]
        self.fecha = dictionary["fecha"]
        self.descripcion = dictionary["descripcion"]
        self.tags=dictionary["tags"]
        self.completada = dictionary["completada"]
        
    def __init__(self, titulo:str, prioridad:int, fecha:str, descripcion:str,tags=[""], completada=False):
        self.titulo = titulo
        self.prioridad=prioridad
        self.fecha = fecha
        self.descripcion = descripcion
        self.tags=tags
        self.completada = completada

    

    def dic(self):
        return vars(self)

    def toJson(self):
        return json.dumps(self.dic(),ensure_ascii = False, indent=2)
    def saveToJson(self):
        io_json.addToJSON(self.dic())
        

