import tarea
import sys
def add():
    if(not ("--nombre" in sys.argv or "--fecha" in sys.argv)): ## mejorar retorno de errores
        raise Exception("No tuviste las suficientes banderas")

    i = sys.argv.index("--nombre")

    print("hola mundo, "+ str(i))

def ls():
    pass
def find():
    pass

print(sys.argv)

match sys.argv[1]:
    case 'add':
        add()
    case 'ls':
        ls()

    case 'find':
        find()

    case default:
        raise Exception("Esa función no está implementada")
    
