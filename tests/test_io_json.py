import json
import app.io_json as io_json
from pathlib import Path


def test_insert_and_list_and_get(tmp_path):
    # storage has been redirected via conftest autouse fixture
    rec1 = io_json.insert_task_dict(
        {
            "titulo": "A",
            "prioridad": 3,
            "fecha": "2025-01-01",
            "descripcion": "",
            "tags": [],
            "completada": False,
        }
    )
    rec2 = io_json.insert_task_dict(
        {
            "titulo": "B",
            "prioridad": 4,
            "fecha": "2025-01-02",
            "descripcion": "",
            "tags": ["x"],
            "completada": False,
        }
    )
    assert rec1["id"] == 1
    assert rec2["id"] == 2

    lst = io_json.list_task_dicts()
    assert {d["titulo"] for d in lst} == {"A", "B"}
    one = io_json.get_task_dict(2)
    assert one["titulo"] == "B"


def test_delete_and_missing():
    rec = io_json.insert_task_dict(
        {
            "titulo": "A",
            "prioridad": 3,
            "fecha": "2025-01-01",
            "descripcion": "",
            "tags": [],
            "completada": False,
        }
    )
    assert io_json.delete_task(rec["id"]) is True
    assert io_json.get_task_dict(rec["id"]) is None
    assert io_json.delete_task(999) is False


def test_load_handles_bad_json(tmp_path, monkeypatch):
    # Point to a specific file and write bad JSON, then ensure load resets store and writes .bak
    monkeypatch.setattr(io_json, "FILE", tmp_path / "tarea.json", raising=True)
    io_json.FILE.write_text("{bad json", encoding="utf-8")
    data = io_json._load_json()
    assert data == {}
    # backup created
    bak = io_json.FILE.with_suffix(io_json.FILE.suffix + ".bak")
    assert bak.exists()
