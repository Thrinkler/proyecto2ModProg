import importlib
import pytest

@pytest.fixture(autouse=True)
def isolate_json_store(tmp_path, monkeypatch):
    """
    Redirect io_json.FILE to a temp file for every test so tests are hermetic.
    """
    import app.io_json as io_json
    # point storage to a temporary JSON file
    monkeypatch.setattr(io_json, "FILE", tmp_path / "tarea.json", raising=True)
    # ensure file exists and is empty JSON object
    io_json._ensure_store()
    # Reload modules that read io_json on import-time if needed
    importlib.reload(io_json)
    importlib.reload(__import__("repo"))
    yield

@pytest.fixture
def add_task():
    """Helper to quickly insert tasks through the public repo API."""
    import app.repo as repo
    from app.tarea import TareaCreate

    def _add(
        titulo="Task",
        prioridad=3,
        fecha="2025-01-01",
        descripcion="",
        tags=None,
    ):
        tc = TareaCreate(
            titulo=titulo,
            prioridad=prioridad,
            fecha=fecha,
            descripcion=descripcion,
            tags=tags or [],
        )
        return repo.add_task(tc)

    return _add
