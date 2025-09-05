import datetime
import io_json
import json

class Tarea:

    @staticmethod
    def returnAll() -> list["Tarea"]:
        task_dictionary = io_json.getArrayFromJSON()
        return [Tarea.from_dict(task) for task in task_dictionary]
    

    @staticmethod
    def find(substr):
        return io_json.findFromJSON(substr)

    @staticmethod
    def save(str):
        pass

    def __init__(
        self,
        id: int,
        titulo: str,
        prioridad: int,
        fecha: str,
        descripcion: str,
        tags=[""],
        completada=False,
    ):
        self.id: int = id
        self.titulo = titulo
        self.prioridad = prioridad
        self.fecha = fecha
        self.descripcion = descripcion
        self.tags = tags
        self.completada = completada

    @classmethod
    def from_dict(cls, dic):
        return cls(
            dic["titulo"],
            dic["prioridad"],
            dic["fecha"],
            dic["descripcion"],
            dic.get("tags", [""]),
            dic.get("completada", False),
        )

    def complete(self):
        self.completada = True

    def toggle(self):
        self.completada = not self.completada

    def delete(self):
        return io_json.deleteFromJSON(self.id)

    def dic(self):
        return vars(self)

    def toJson(self):
        return json.dumps(self.dic(), ensure_ascii=False, indent=2)

    def saveToJson(self):
        io_json.addToJSON(self.dic())
