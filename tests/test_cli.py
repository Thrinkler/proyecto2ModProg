import sys
import io
import json
import builtins
import importlib

import pytest

def run_main(argv):
    # late import to ensure fixtures patched modules before loading main
    import app.main as main
    old = sys.argv[:]
    sys.argv = ["tikitiki"] + argv
    try:
        main.main()
    finally:
        sys.argv = old

def capture_run(argv, capsys):
    run_main(argv)
    return capsys.readouterr().out

def test_cli_add_and_ls(capsys):
    out = capture_run(["add", "Task One", "-p", "5", "-dt", "2025-09-09", "-d", "desc", "-t", "work", "urgent"], capsys)
    assert "Task added successfully." in out

    out = capture_run(["ls"], capsys)

    # should print JSON per task
    lines = [ln for ln in out.splitlines() if ln.strip().startswith("{")]
    assert len(lines) == 1
    d = json.loads(out)
    assert d["titulo"] == "Task One"
    assert d["prioridad"] == 5
    assert d["fecha"] == "2025-09-09"
    assert d["tags"] == ["work", "urgent"]

def test_cli_find_and_sort(capsys):
    capture_run(["add", "A", "-p", "2", "-dt", "2025-01-01", "-d", "x"], capsys)
    capture_run(["add", "B", "-p", "4", "-dt", "2025-01-02", "-d", "bbb"], capsys)
    capture_run(["add", "C", "-p", "1", "-dt", "2025-01-03", "-d", "ccc"], capsys)

    out = capture_run(["find", "b", "--sort", "priority"], capsys)
    titles = [json.loads(ln)["titulo"] for ln in out.splitlines() if ln.strip().startswith("{")]
    assert titles == ["C", "B"]  # priorities 1 then 4

def test_cli_complete_and_filters(capsys):
    capture_run(["add", "Do it", "-dt", "2025-01-01"], capsys)
    capture_run(["add", "Done already", "-dt", "2025-01-01"], capsys)
    # Complete id=2
    capture_run(["complete", "2"], capsys)

    out_all = capture_run(["ls", "--all"], capsys)
    assert sum(1 for ln in out_all.splitlines() if ln.strip().startswith("{")) == 2

    out_incomplete = capture_run(["ls"], capsys)
    assert sum(1 for ln in out_incomplete.splitlines() if ln.strip().startswith("{")) == 1

    out_completed_only = capture_run(["ls", "--completed"], capsys)
    lines = [ln for ln in out_completed_only.splitlines() if ln.strip().startswith("{")]
    assert len(lines) == 1 and json.loads(lines[0])["completada"] is True

def test_cli_parser_rejects_bad_date():
    # Test the argparse type directly via cli.date_yyyy_mm_dd
    import argparse
    from app.cli import date_yyyy_mm_dd
    with pytest.raises(argparse.ArgumentTypeError):
        date_yyyy_mm_dd("2025/01/01")

@pytest.mark.xfail(reason="repo.save_task is not implemented and signature mismatch")
def test_cli_save_xfail(capsys):
    out = capture_run(["save", "out.json"], capsys)
    # Expect implementation later; this test marks desired behavior
    assert "Saved" in out
