import datetime
class Tarea:

    dic = {
        "id" : 0,
        "titulo" : "",
        "prioridad" : 0,
        "fecha": datetime.datetime(2020,1,1),
        "descripcion" : "",
        "completada" : False
    }


    def __init__(self, idval:int, titulo:str, prioridad:int, fecha:datetime,descripcion:str,completada:bool):

        self.dic["id"] = idval
        self.dic["titulo"] = titulo
        self.dic["prioridad"]=prioridad
        self.dic["fecha"] = fecha
        self.dic["descripcion"] = descripcion
        self.dic["completada"] = completada

    def fromDic():
        pass

    def fromJson():
        pass
    def toJson():
        pass ##Json.dump()
    