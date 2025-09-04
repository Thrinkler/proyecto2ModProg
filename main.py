import cli
from tarea import Tarea

def main():
    parser = cli.start_parser()
    args = parser.parse_args()
    print(args)
    
    if args.command == "add":
        tarea = Tarea(args.title, args.priority, args.date, args.description, args.completed)
        tarea.saveToJson()
        print("Task added successfully.")

if __name__ == "__main__":
    main()
    
