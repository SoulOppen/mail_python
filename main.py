def main():
    tasks=["Modificar excel","Obtener data estadística de excel","Enviar mail masivos con outlook","Enviar whatsApp"]
    print("Bienvenido a tu administrador de tareas repetitivas en windows")
    print("Las tareas que podemos administrar hasta el momento son:")
    for i,task in enumerate(tasks):
        print(f"\t{i+1}-{task}")
if __name__=="__main__":
    main()