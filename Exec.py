from Logica import *

def Menu():
 
    correcto=False
    num=0
    while(not correcto):
        try:
            num = int(input("Elige una opción: "))
            correcto=True
        except ValueError:
            print('Introduce una opción correcta')
    return num
salir = False
opcion = 0
while not salir:
    print("---------------------------------------------------------")
    print("1. Mostrar todo")
    print("2. Insertar libro")
    print("3. Eliminar libro por ID")
    print("4. Actualizar copias")
    print("5. Mostrar ordenados por autor")
    print("6. Mostrar ordenados por titulo")
    print("7. Mostrar ordenados por editorial")
    print("8. Salir")
    
    opcion = Menu()
    if opcion == 1:
        mostrarTodo()   
    elif opcion == 2:
        insertar()
    elif opcion == 3:
        eliminar()
    elif opcion == 4:
        actualizarCopias()
    elif opcion == 5:
        ordenarAutor()
    elif opcion == 6:
        ordenarTitulo()
    elif opcion == 7:
        ordenarEditorial()
    elif opcion == 8:
        salir = True
    else:
        print ('Introduce una opción correcta')
print ("Saliendo")