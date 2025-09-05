import cli
from tarea import Tarea

def main():
    parser = cli.start_parser()
    args = parser.parse_args()
    #print(args)

    match args.command:
        case "add":
            tarea = Tarea(args.title, args.priority, args.date, args.description, args.tags, args.completed)
            tarea.saveToJson()
            print("Task added successfully.")
        case "ls":
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

        case "find":
            if args.string:
                tareas = Tarea.locate(args.string)
                for tarea in tareas:
                    print(tarea)
            else:
                print("Please provide a substring to search for.")

        case "complete":
            if args.filename:
                tarea = Tarea.get(args.id)
                tarea.complete()
            else:
                print("Please provide a task ID to complete.")
        case "delete":
            if args.filename:
                tarea = Tarea.get(args.id)
                tarea.complete()
            else:
                print("Please provide a task ID to complete.")
        case "save":
            if args.filename:
                Tarea.save(args.filename)
            else:
                print("Please provide a filename to save tasks.")

        case default:
            print("TikiTiki Agenda: error: No command provided. Use -h for help. (choose from add, ls, find, complete, delete, save)")
if __name__ == "__main__":
    main()
    
