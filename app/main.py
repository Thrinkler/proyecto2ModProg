import cli
from tarea import Tarea, TareaCreate
import repo as repo

def main():
    parser = cli.start_parser()
    args = parser.parse_args()
    #print(args)

    match args.command:
        case "add":
            tarea = TareaCreate(
                titulo=args.title,
                prioridad=args.priority,
                fecha=args.date,
                descripcion=args.description,
                tags=args.tags
            )
            repo.add_task(tarea)
            print("Task added successfully.")
        case "ls":
            tareas = repo.get_task_list()

            if args.filter:
                tareas = [t for t in tareas if any(tag in t.get("tags", []) for tag in args.filter)]
            
            if not args.all:
                tareas = [t for t in tareas if not t.completada]
            
            if args.completed:
                tareas = [t for t in tareas if t.completada]
            
            print(tarea.fecha for tarea in tareas)
            if args.sort == "date":
                tareas.sort(key=lambda x: x.fecha, reverse=args.reverse)
            elif args.sort == "priority":
                tareas.sort(key=lambda x: x.prioridad, reverse=args.reverse)
            elif args.sort == "title":
                tareas.sort(key=lambda x: x.titulo, reverse=args.reverse)

            for tarea in tareas:
                print(tarea.to_json())

        case "find":
            if args.string:
                tareas = repo.find_tasks(args.string)
                for tarea in tareas:
                    print(tarea.to_json())
            else:
                print("Please provide a substring to search for.")

        case "complete":
            if args.id:
                repo.complete_task(args.id)
                print(f"Task {args.id} marked as completed.")
            else:
                print("Please provide a task ID to complete.")
        case "delete":
            if args.id:
                repo.delete_task(args.id)
                print(f"Task {args.id} deleted successfully.")
            else:
                print("Please provide a task ID to complete.")
        case "save":
            if args.filename:
                repo.save_task(args.filename)
            else:
                print("Please provide a filename to save tasks.")

        case default:
            print("TikiTiki Agenda: error: No command provided. Use -h for help. (choose from add, ls, find, complete, delete, save)")
if __name__ == "__main__":
    main()
    
