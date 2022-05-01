#Importo la clase de Personaje y llamo el objeto Personaje
from clases.Ciclista import Ciclista

#Listas
ciclistas = []

def menu():
    print("\nCompetencia Ciclismo") 
    print("**********************************************") 
    print("0. Salir") 
    print("1. Ingresar Ciclista") 
    print("2. Mostrar mejor tiempo") 
    print("3. Mostrar Todos los datos") 
    print("**********************************************\n") 

opcion = 1 
 
while(opcion != 0): 
    menu()
    opcion = int(input("Digita una opcion: ")) 
    #pregunte por la opcion 
    if(opcion == 0): 
        break 
    elif(opcion == 1):
        nombre = input("Nombre: ")
        edad = int(input("Edad: "))
        pais = input("Pais: ")
        tiempo = int(input("Tiempo: "))

        ciclistas.append(Ciclista(nombre, edad, pais, tiempo))
    elif(opcion == 2): 
        mejorTiempo = ciclistas[0].tiempo
        for ciclista in ciclistas:
            if(ciclista.tiempo < mejorTiempo):
                mejorTiempo = ciclista.tiempo
        print(f"el mejor tiempo es: {mejorTiempo}")    
        print("-------------------------")
        input("Press enter for continue >> ")
        print("-------------------------")
    elif(opcion == 3):
        for i in range(len(ciclistas)):
            print(ciclistas[i])
        print("-------------------------")
        input("Press enter for continue >> ")
        print("-------------------------")
    else: 
        print("Debe ingresar un numero")
        menu()