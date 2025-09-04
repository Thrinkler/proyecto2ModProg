import argparse
from datetime import date

def date_yyyy_mm_dd(s: str) -> str:
    try:
        date.fromisoformat(s)
    except ValueError as e:
        raise argparse.ArgumentTypeError(f"Not a valid date: '{s}'. Expected format: YYYY-MM-DD") from e
    
    return s

def start_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="PixelPlanner", description="The best task manager... If it were the 80s.", epilog="Developed by Manuel Sandoval Arroyo & Arturo Espejel Baez")
    parent = argparse.ArgumentParser(add_help=False)
    
    subparser = parser.add_subparsers(dest="command", required=True)

    # Add

    add = subparser.add_parser("add", parents=[parent], help="Add a new task")
    add.add_argument("title", type=str, help="Name of the task")
    add.add_argument("-d", "--description", type=str, default="", help="Description of the task")
    add.add_argument("-p", "--priority", type=int, choices=range(1, 6), default=3, help="Priority of the task (1-5)")
    add.add_argument("-dt", "--date", type=date_yyyy_mm_dd, default=date.today().isoformat(), help="Due date of the task (YYYY-MM-DD)")
    add.add_argument("-t", "--tags", type=str, nargs="*", default=[], help="Tags for the task")
    add.add_argument("-c", "--completed", action="store_true", help="Mark the task as completed")
    # ls
    ls = subparser.add_parser("ls", parents=[parent], help="List all tasks")
    ls.add_argument("-s", "--sort", type=str, choices=["date", "priority", "title"], default="date", help="Sort tasks by (date, priority, title)")
    ls.add_argument("-f", "--filter", type=str, nargs="*", default=[], help="Filter tasks by tags")
    ls.add_argument("-r", "--reverse", help="Reverse the sort order", action="store_true")
    ls.add_argument("-a", "--all", help="Show all tasks including completed ones", action="store_true")
    ls.add_argument("-c", "--completed", help="Show only completed tasks", action="store_true")

    return parser
