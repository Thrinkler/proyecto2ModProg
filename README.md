# TikiTiki Agenda

## The best agenda... for the TikiTiki island.

To start working with it (beta), type on the terminal inside 
the main folder:

    python3 -m app.main [-h] {add,ls,find,complete,delete,save}

To export the html file:

    python3 -m app.export_html

Functions:

    add                 Add a new task
        -h, --help            show its help message and exit
        -d, --description DESCRIPTION
                        Description of the task
        -p, --priority {1,2,3,4,5}
                        Priority of the task (1-5)
        -dt, --date DATE      Due date of the task (YYYY-MM-DD)
        -t, --tags [TAGS ...]
                        Tags for the task
        -c, --completed       Mark the task as completed
        
    ls                  List all tasks
        -h, --help            show its help message and exit
        -s, --sort {date,priority,title}
                                Sort tasks by (date, priority, title)
        -f, --filter [FILTER ...]
                                Filter tasks by tags
        -r, --reverse         Reverse the sort order
        -a, --all             Show all tasks including completed ones
        -c, --completed       Show only completed tasks
        
    find                find tasks by substring
        -h, --help            show its help message and exit
        -s, --sort {date,priority,title}
                        Sort tasks by (date, priority, title)
                        
    complete            Mark a task as completed
        positional arguments:
            id          ID of the task to mark as completed
        options:
            -h, --help  show its help message and exit
            
    delete              Delete a task
    positional arguments:
        id          ID of the task to delete
        options:
        -h, --help  show its help message and exit
        
    save                Save tasks to a file
        positional arguments:
            filename    Filename to save tasks to
        options:
            -h, --help  show its help message and exit

Developed by Manuel Sandoval Arroyo & Juan Arturo Espejel Baez
