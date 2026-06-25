MostrarMenu = True
tareas = []

def val_descripcion(descripcion):

    descripcion_norm = descripcion.strip()

    if len(descripcion_norm) > 0:
        return True
    else:
        return False  

def val_prioridad(prioridad):
    
    if prioridad>0:
        return True
    else:
        return False
def val_tiempo(tiempo_estimado):
    if tiempo_estimado > 0:
        return True
    else:
        return False
    
def buscar_tarea(descripcion):
    for i in range(len(tareas)):
        if tareas[i]['descripcion'] == descripcion:
            return i 
    return -1
def estado_tareas(tareas):
    for tarea in tareas:
        if tarea['prioridad'] >= 5:
            tarea['completada'] = True
    else:
        
        tarea['completada'] = False

def mostrartareas(tareas):
     
    print("Descripcion de la tarea: ",tarea['descripcion']) 
    print("Prioridad: ",tarea['prioridad'])
    print("Tiempo estimado: ",tarea['tiempo estimado'])
    print("Estado: ",tarea['completada'])
    print("************************************")
    

def menu():
    print(" opcion 1) Agregar tarea")
    print(" opcion 2) Buscar tarea ")
    print(" opcion 3) Eliminar tarea ")
    print(" opcion 4) Actualizar estado ")
    print(" opcion 5) Mostrar tareas ")
    print(" opcion 6) salir ")
    

def Registrar_tarea(tareas):
        descripcion = input(" Ingrese la descripcion de la tarea: ")
        if val_descripcion(descripcion) == True:
            try:
                prioridad = int(input("Ingrese la prioridad de la tarea en una escala de 1 a 10: "))
                val_prioridad(prioridad)
                if val_prioridad(prioridad) == True:
                    try:
                        tiempo_estimado = int(input("Ingrese el tiempo estimado en HORAS: "))
                        if val_tiempo(tiempo_estimado) == True:
                            completada = False
                            tarea = {
                                'descripcion':  descripcion,
                                'prioridad': prioridad,
                                'tiempo estimado': tiempo_estimado,
                                'completada': completada
                            }
                            tareas.append(tarea)
                            return True
                        else:
                            print("el tiempo estimado no puede ser menor a 0")
                            return False

                    except ValueError:
                        print("El tiempo estimado ingresado debe ser un numero entero positivo")
                        return False
                else:
                    print("La prioridad ingresada no puede ser 0 ")
                    return False
            except ValueError:
                print("La prioridad de la tarea debe ser ingresada en numeros enteros entre 1 a 10")
                return False
        else:
            print("La descripcion ingresada no puede estar vacia ni contener solo espacios")
            return False
    



while MostrarMenu == True:

    menu()
    opcion = input("Ingrese la opcion deseada: ")

    if opcion == '1':
        if Registrar_tarea(tareas) == True:
            print("Tarea registrada correctamente")
        else:
            print("La tarea no se registro")

    elif opcion == '2':
        descripcion = input("Ingrese la descripcion de la tarea a buscar: ")
        buscar_tarea(descripcion)
        encontrado = False
        for tarea in tareas:
            if tarea ['descripcion'] == descripcion:
                encontrado = True
                mostrartareas(tareas)
        if encontrado == False:
            print("la tarea no se pudo encontrar")

    elif opcion == '3':

        descripcion_a_eliminar = input("Ingrese la descripcion de la tarea a eliminar: ")
        eliminar = buscar_tarea(descripcion_a_eliminar)
        if eliminar != -1:
            tareas.pop(eliminar)
        else:
            print("Tarea no encontrada")

    elif opcion == '4':
        if len(tareas)> 0:  
            print("todas los estados de las tareas registradas fueron actualizadas segun los requisitos. ")
            estado_tareas(tareas)
        else:
            print("No se registraron tareas aun")     

    elif opcion == '5':
        if len(tareas)> 0:  
            print("Las tareas registradas son las siguientes: ")
            for tarea in tareas:
                mostrartareas(tarea)
        else:
            print("No se registraron tareas aun")      
    elif opcion == '6':
        print("Saliendo del programa ")
        MostrarMenu = False
    else:
        print("la opcion ingresada no es valida")
