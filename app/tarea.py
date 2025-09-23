import json
from dataclasses import dataclass
from datetime import date
from typing import Optional, List, Dict, Any


@dataclass
class TareaBase:
    titulo: str
    prioridad: int
    fecha: str
    descripcion: str
    tags: Optional[List[str]] = None
    completada: bool = False

    def to_dict(self) -> Dict[str, Any]:
        return self.__dict__
    
    def to_json(self) -> str:
        return json.dumps(self.to_dict(), ensure_ascii=False, indent=2)

@dataclass
class TareaCreate(TareaBase):

    def __post_init__(self):
        if self.tags is None:
            self.tags = []

        if not self.titulo:
            raise ValueError("title is required")
        if not self.prioridad in range(1, 6):
            raise ValueError("priority must be between 1 and 5")

        try:
            date.fromisoformat(self.fecha)
        except ValueError as e:
            raise ValueError(f"date must be in YYYY-MM-DD format: {self.fecha}") from e

        if self.descripcion is None:
            self.descripcion = ""

        self.titulo = self.titulo.strip()
        self.descripcion = self.descripcion.strip()
        self.tags = [tag.strip() for tag in self.tags if tag.strip()]

@dataclass
class Tarea(TareaBase):
    id: int = 0

    @classmethod
    def from_dict(cls, dic:Dict[str, Any]) -> "Tarea":
        tarea = cls(
            titulo=dic["titulo"],
            prioridad=dic["prioridad"],
            fecha=dic["fecha"],
            descripcion=dic["descripcion"],
            tags=dic.get("tags", [""]),
            completada=dic.get("completada", False)
        )
        tarea.id = dic["id"]
        return tarea

    def complete(self) -> None:
        self.completada = True

    def toggle(self) -> None:
        self.completada = not self.completada


    def to_dict(self) -> Dict[str, Any]: 
        return  {"id": self.id, **super().to_dict()}
