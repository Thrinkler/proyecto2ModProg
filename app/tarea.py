import json
from dataclasses import dataclass
from datetime import date
from typing import Optional, List, Dict, Any


class Tarea:
    id = 0
    def __init__(
        self,
        titulo: str,
        prioridad: int,
        fecha: str,
        descripcion: str,
        tags: List[str] = None,
        completada: bool = False,
    ):
        if(not (1 <= prioridad <= 5)):
            raise ValueError("Priority must be between 1 and 5")
        self.titulo = titulo
        self.prioridad = prioridad
        self.fecha = fecha  # keep as ISO string if that’s your contract
        self.descripcion = descripcion
        self.tags = list(tags) if tags is not None else []  # defensive copy
        self.completada = completada

    @classmethod
    def from_dict(cls, dic:Dict[str, Any]) -> "Tarea"):
        
        tarea = cls(
            dic["titulo"],
            dic["prioridad"],
            dic["fecha"],
            dic["descripcion"],
            dic.get("tags", [""]),
            dic.get("completada", False)
        )
        tarea.id = dic["id"]
        return tarea

    def complete(self) -> None:
        self.completada = True

    def toggle(self) -> None:
        self.completada = not self.completada


    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "titulo": self.titulo,
            "prioridad": self.prioridad,
            "fecha": self.fecha,
            "descripcion": self.descripcion,
            "tags": list(self.tags),  # avoid exposing internal list
            "completada": self.completada,
        }

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), ensure_ascii=False, indent=2)


@dataclass
class TareaCreate:
    titulo: str
    prioridad: int
    fecha: str
    descripcion: str
    tags: Optional[List[str]] = None

    def __post_init__(self):
        if self.tags is None:
            self.tags = []

        if not self.titulo:
            raise ValueError("titulo is required")
        if not self.prioridad in range(1, 6):
            raise ValueError("prioridad must be between 1 and 5")

        try:
            date.fromisoformat(self.fecha)
        except ValueError as e:
            raise ValueError(f"fecha must be in YYYY-MM-DD format: {self.fecha}") from e

        if self.descripcion is None:
            self.descripcion = ""

        self.titulo = self.titulo.strip()
        self.descripcion = self.descripcion.strip()
        self.tags = [tag.strip() for tag in self.tags if tag.strip()]

    def to_dict(self) -> Dict[str, Any]:
        # Handy when passing to persistence layer
        return {
            "titulo": self.titulo,
            "prioridad": self.prioridad,
            "fecha": self.fecha,
            "descripcion": self.descripcion,
            "tags": self.tags or [],
            "completada": False,  # enforce default on creation
        }
    def to_json(self):
        return json.dumps({"id": self.id, **self.dic()}, ensure_ascii=False, indent=2)
