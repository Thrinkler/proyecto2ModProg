import datetime
import io_json
import json

class Tarea:
    id = 0
    def __init__(
        self,
        titulo: str,
        prioridad: int,
        fecha: str,
        descripcion: str,
        tags=[],
        completada=False,
    ):
        if(not (1 <= prioridad <= 5)):
            raise ValueError("Priority must be between 1 and 5")
        self.titulo = titulo
        self.prioridad = prioridad
        self.fecha = fecha
        self.descripcion = descripcion
        self.tags = tags
        self.completada = completada

    @classmethod
    def from_dict(cls, dic):
        
        tarea = cls(
            dic["titulo"],
            dic["prioridad"],
            dic["fecha"],
            dic["descripcion"],
            dic.get("tags", [""]),
            dic.get("completada", False),
        )
        tarea.id = dic["id"]
        return tarea

    def complete(self):
        self.completada = True

    def toggle(self):
        self.completada = not self.completada
    
    def dic(self):
        return vars(self)

    def to_json(self):
        return json.dumps({"id": self.id, **self.dic()}, ensure_ascii=False, indent=2)
