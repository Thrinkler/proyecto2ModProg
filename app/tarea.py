import datetime
import io_json
import json

class Tarea:
    def __init__(
        self,
        id: int,
        titulo: str,
        prioridad: int,
        fecha: str,
        descripcion: str,
        tags=[],
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
            dic["id"],
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
    
    def dic(self):
        return vars(self)

    def to_json(self):
        return json.dumps(self.dic(), ensure_ascii=False, indent=2)
