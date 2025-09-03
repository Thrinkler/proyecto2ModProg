import datetime
import json
class Tarea:

    dic = {
        "id" : 0,
        "titulo" : "",
        "prioridad" : 0,
        "fecha": "",
        "descripcion" : "",
        "completada" : False
    }


    def __init__(self, idval:int, titulo:str, prioridad:int, fecha:str,descripcion:str,completada:bool):

        self.dic["id"] = idval
        self.dic["titulo"] = titulo
        self.dic["prioridad"]=prioridad
        self.dic["fecha"] = fecha
        self.dic["descripcion"] = descripcion
        self.dic["completada"] = completada

    def fromDic():
        pass

    def returnDic(self):
        return self.dic

    def fromJson():
        pass
    def toJson(self):
        return json.dumps(self.dic,ensure_ascii = False, indent=2)
    def saveToJson(self):
        with open("tarea.json", "w",encoding="UTF-8") as f:
            self.toJson()

    

tarea = Tarea(0,"Mi primera tarea",0,str(datetime.datetime.now().date()),"Es mi primera tarea.",False)
print(tarea.toJson())
tarea.saveToJson()