import cli
from tarea import Tarea
import repo

def main():
    parser = cli.start_parser()
    args = parser.parse_args()
    #print(args)

    match args.command:
        case "add":
            tarea = Tarea(args.title, args.priority, args.date, args.description, args.tags, args.completed)
            repo.addTask(tarea)
            print("Task added successfully.")
        case "ls":
            tareas = repo.getTaskList()
            
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
                tareas = repo.findTasks(args.string)
                for tarea in tareas:
                    print(tarea)
            else:
                print("Please provide a substring to search for.")

        case "complete":
            if args.id:
                repo.completeTask(args.id)
                print(f"Task {args.id} marked as completed.")
            else:
                print("Please provide a task ID to complete.")
        case "delete":
            if args.id:
                repo.deleteTask(args.id)
                print(f"Task {args.id} deleted successfully.")
            else:
                print("Please provide a task ID to complete.")
        case "save":
            if args.filename:
                repo.saveTask(args.filename)
            else:
                print("Please provide a filename to save tasks.")

        case default:
            print("TikiTiki Agenda: error: No command provided. Use -h for help. (choose from add, ls, find, complete, delete, save)")
if __name__ == "__main__":
    main()
    
