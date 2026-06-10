# En el archivo Personaje_clase.py desarrollar la clase Personaje  con #atributo de clase "estado = True" #vivo.
# Y el constructor y los atributos (nombre, altura, velocidad, resistencia, fuerza) y dos metodos, correr y recuperarse.

class Personaje:
    def __init__(self, nombre, altura, velocidad, resistencia, fuerza):
        self.nombre = nombre
        self.altura = altura
        self.velocidad = velocidad
        self.resistencia = resistencia
        self.fuerza = fuerza
        self.estado = True 
    
    def correr(self):
        if self.estado == True:
            distancia = 1000
            tiempo = distancia / self.velocidad 
            self.estado = False
            return tiempo
        else:
            print("El personaje esta cansado")
            return None
           
    def recuperarse(self):
        self.estado = True
