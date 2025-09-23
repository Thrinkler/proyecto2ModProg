import pytest
from datetime import date

from tarea import Tarea, TareaCreate

def test_tarea_create_validates_and_normalizes():
    tc = TareaCreate(
        titulo="  Hello  ",
        prioridad=5,
        fecha="2025-09-09",
        descripcion="  world ",
        tags=["  a ", " ", "b"],
    )
    assert tc.titulo == "Hello"
    assert tc.descripcion == "world"
    assert tc.tags == ["a", "b"]
    assert tc.to_dict()["completada"] is False

@pytest.mark.parametrize("bad_priority", [0, 6])
def test_tarea_create_rejects_bad_priority(bad_priority):
    with pytest.raises(ValueError):
        TareaCreate(titulo="x", prioridad=bad_priority, fecha="2025-01-01", descripcion="")

@pytest.mark.parametrize("bad_date", ["2025/01/01", "01-01-2025", "2025-13-01"])
def test_tarea_create_rejects_bad_date(bad_date):
    with pytest.raises(ValueError):
        TareaCreate(titulo="x", prioridad=3, fecha=bad_date, descripcion="")

def test_tarea_complete_and_toggle():
    t = Tarea("X", 3, "2025-01-01", "")
    assert t.completada is False
    t.complete()
    assert t.completada is True
    t.toggle()
    assert t.completada is False

def test_tarea_dict_roundtrip():
    t = Tarea("X", 2, "2025-01-01", "desc", tags=["a"])
    t.id = 7
    d = t.to_dict()
    t2 = Tarea.from_dict(d)
    assert t2.id == 7
    assert t2.titulo == "X"
    assert t2.prioridad == 2
    assert t2.fecha == "2025-01-01"
    assert t2.descripcion == "desc"
    assert t2.tags == ["a"]
