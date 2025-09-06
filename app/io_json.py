import json
from pathlib import Path
from typing import Dict, Any, List, Optional

FILE = Path("tarea.json")  # or Path(__file__).with_name("tarea.json")


def _ensure_store() -> None:
    """Make sure the parent folder and JSON file exist."""
    FILE.parent.mkdir(parents=True, exist_ok=True)
    if not FILE.exists():
        FILE.write_text("{}", encoding="utf-8")  # start as empty object


def _load_json() -> Dict[str, Any]:
    _ensure_store()
    content = FILE.read_text(encoding="utf-8").strip()
    if not content:
        return {}  # empty file → treat as empty store
    try:
        return json.loads(content)
    except json.JSONDecodeError:
        # Backup the bad file and reset to {}
        FILE.with_suffix(FILE.suffix + ".bak").write_text(content, encoding="utf-8")
        FILE.write_text("{}", encoding="utf-8")
        return {}


def _save_json(data: Dict[str, Any]) -> None:
    _ensure_store()
    # atomic-ish write: write to temp then replace
    tmp = FILE.with_suffix(FILE.suffix + ".tmp")
    tmp.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    tmp.replace(FILE)


def get_task_dict(task_id: int) -> Optional[Dict[str, Any]]:
    data = _load_json()
    rec = data.get(str(task_id))
    return {"id": task_id, **rec} if rec else None


def list_task_dicts() -> List[Dict[str, Any]]:
    data = _load_json()
    # keys are strings in JSON; expose id as int in returned dicts
    return [{"id": int(k), **v} for k, v in data.items()]


def _next_id(data: Dict[str, Any]) -> int:
    if not data:
        return 1
    return max(int(k) for k in data.keys()) + 1


def insert_task_dict(payload: Dict[str, Any]) -> Dict[str, Any]:
    data = _load_json()
    task_id = _next_id(data)
    data[str(task_id)] = {k: v for k, v in payload.items() if k != "id"}
    _save_json(data)
    return {"id": task_id, **data[str(task_id)]}


def upsert_task_dict(task: Dict[str, Any]) -> Dict[str, Any]:
    """Update or insert by id (id required)."""
    if "id" not in task:
        raise ValueError("upsert_task_dict requires 'id'")
    data = _load_json()
    task_id = int(task["id"])
    data[str(task_id)] = {k: v for k, v in task.items() if k != "id"}
    _save_json(data)
    return {"id": task_id, **data[str(task_id)]}


def delete_task(task_id: int) -> bool:
    data = _load_json()
    key = str(task_id)
    if key in data:
        del data[key]
        _save_json(data)
        return True
    return False
