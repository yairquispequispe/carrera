# Crear una carpeta de trabajo, llamada "POO"
# Dentro de esa carpeta crear dos archivos .py 
# uno llamado carrera.py y otro Personaje_clase.py
# En el archivo Personaje_clase.py desarrollar la clase Personaje  con 
# #atributo de clase "estado = True" #vivo.
# Y el constructor y los atributos (nombre, altura, velocidad, resistencia, fuerza) 
# y dos metodos, correr y recuperarse.
#Luego en el archivo carrera.py 
# crear un menu: 
# "ingresar participantes"pedirle los datos al usuario para instanciar objetos e imprimirlos por pantalla, "correr carrera" "pedir distancia" y realizar la carrera, "salir"
from personajes import Personaje

menu = '''
1 - crear personaje 1
2 - crear personaje 2
3 - correr carrera
4 - salir'''

personaje1 = None
personaje2 = None

while True:
    print(menu)
    opcion = input("Ingrese una opcion: ")
    
    if opcion == "1":
        nombre = input("ingrese el nombre del personaje 1: ")
        altura = float(input("Ingrese la altura promedia del personaje 1: "))
        velocidad = float(input("Ingrese la velocidad del personaje 1: "))
        resistencia = float(input("Ingrese el valor de la resistencia del personaje 1: "))
        fuerza = float(input("Ingrese la fuerza del personaje 1: "))
        
        personaje1 = Personaje(nombre, altura, velocidad, resistencia, fuerza)
        print("Personaje 1 creado con éxito.")
        
    elif opcion == "2":
        nombre = input("ingrese el nombre del personaje 2: ")
        altura = float(input("Ingrese la altura promedia del personaje 2: "))
        velocidad = float(input("Ingrese la velocidad del personaje 2: "))
        resistencia = float(input("Ingrese el valor de la resistencia del personaje 2: "))
        fuerza = float(input("Ingrese la fuerza del personaje 2: "))
        
        personaje2 = Personaje(nombre, altura, velocidad, resistencia, fuerza)
        print("Personaje 2 creado con éxito.")
        
    elif opcion == "3":
        if personaje1 is not None and personaje2 is not None:
            tiempo1 = personaje1.correr()
            tiempo2 = personaje2.correr()
            print("El personaje 1 demoro:", tiempo1)
            print("El personaje 2 demoro:", tiempo2)
        else:
            print("Primero debes crear ambos personajes (opciones 1 y 2).")
    
    elif opcion == "4":
        break
        
    else:
        print("Opción no válida.")
