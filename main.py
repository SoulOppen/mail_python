from config import Task,Basic 
from exit import exit
def main():
    print("Bienvenido a tu administrador de tareas repetitivas en windows")
    print("Las tareas que podemos administrar hasta el momento son:")
    tasks=Task+Basic
    for i,task in enumerate(tasks):
        print(f"\t{i+1}-{task}")
    try:
        input_number=int(input("Numero de tarea: "))
        if tasks[input_number-1]=="Exit":
            exit()
    except ValueError:
        print("Debes ingresar un número válido.")
        main()
if __name__=="__main__":
    main()