import json
from pathlib import Path
from typing import Dict, Any, List, Optional

FILE = Path("tarea.json")

def _load_json() -> Dict[str, Any]:
    if not FILE.exists():
        return {}
    content = FILE.read_text(encoding="utf-8").strip()
    return json.loads(content) if content else {}

def _save_json(data: Dict[str, Any]) -> None:
    FILE.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

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
