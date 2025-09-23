import importlib
import pytest


@pytest.fixture(autouse=True)
def isolate_json_store(tmp_path, monkeypatch):
    """
    Redirect io_json.FILE to a temp file and clear any in-memory cache.
    """
    import app.io_json as io_json

    # --- THIS IS THE CRUCIAL NEW STEP ---
    # Manually reset the module's in-memory cache before each test.
    # NOTE: You must find the actual name of the variable in your
    # app/io_json.py that holds the data. It might be _DATA, _cache, _tasks, etc.
    if hasattr(io_json, "_DATA"):  
        monkeypatch.setattr(io_json, "_DATA", {})
    monkeypatch.setattr(io_json, "FILE", tmp_path / "tarea.json", raising=True)
    io_json._ensure_store()

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
