import sys
import json

import pytest


def run_main(argv):
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
    out = capture_run(
        [
            "add",
            "Task One",
            "-p",
            "5",
            "-dt",
            "2025-09-09",
            "-d",
            "desc",
            "-t",
            "work",
            "urgent",
        ],
        capsys,
    )
    assert "Task added successfully." in out

    out = capture_run(["ls"], capsys)
    lines = [ln for ln in out.splitlines() if ln.strip().startswith("{")]
    assert len(lines) == 1
    d = json.loads(out)
    assert d["titulo"] == "Task One"
    assert d["prioridad"] == 5
    assert d["fecha"] == "2025-09-09"
    assert d["tags"] == ["work", "urgent"]


def test_cli_parser_rejects_bad_date():
    import argparse
    from app.cli import date_yyyy_mm_dd
    with pytest.raises(argparse.ArgumentTypeError):
        date_yyyy_mm_dd("2025/01/01")


