from app.tarea import Tarea, TareaCreate
import app.repo as repo



def test_add_and_get(add_task):
    t = add_task(titulo="Alpha", prioridad=3, fecha="2025-01-01")
    fetched = repo.get_task(t.id)
    assert fetched is not None
    assert fetched.titulo == "Alpha"
    assert fetched.completada is False


def test_complete_flow(add_task):
    t = add_task(titulo="Go", prioridad=4, fecha="2025-02-02")
    out = repo.complete_task(t.id)
    assert out is not None and out.completada is True


def test_find_tasks(add_task):
    add_task(titulo="Do groceries", descripcion="milk and eggs", fecha="2025-01-01")
    add_task(titulo="Email", descripcion="follow up", fecha="2025-01-01")
    hits = repo.find_tasks("milk")
    assert len(hits) == 1 and "groceries" in hits[0].titulo.lower()


def test_delete_task(add_task):
    t = add_task(titulo="Temp", prioridad=2, fecha="2025-01-03")
    deleted = repo.delete_task(t.id)
    assert deleted is not None and deleted.id == t.id
    assert repo.get_task(t.id) is None
