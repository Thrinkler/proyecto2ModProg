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
    elif args.command == "ls":
        tareas = Tarea.returnAll()
        
        if args.filter:
            tareas = [t for t in tareas if any(tag in t.get("tags", []) for tag in args.filter)]
        
        if not args.all:
            tareas = [t for t in tareas if not t["completada"]]
        
        if args.completed:
            tareas = [t for t in tareas if t["completada"]]
        
        if args.sort == "date":
            tareas.sort(key=lambda x: x["fecha"], reverse=args.reverse)
        elif args.sort == "priority":
            tareas.sort(key=lambda x: x["prioridad"], reverse=args.reverse)
        elif args.sort == "title":
            tareas.sort(key=lambda x: x["titulo"], reverse=args.reverse)
        
        for tarea in tareas:
            print(Tarea(tarea).toJson())
    elif args.command == "find":
        if args.string:
            tareas = Tarea.locate(args.string)
            for tarea in tareas:
                print(tarea)
        else:
            print("Please provide a substring to search for.")
if __name__ == "__main__":
    main()
    
