class Ciclista:

    def __init__(self, nombre, edad, pais, tiempo):
        self.__nombre = nombre
        self.__edad = edad
        self.__pais = pais
        self.__tiempo = tiempo

    def __str__(self):
        return "name: " + self.__nombre + " | age: " + str(self.__edad) + " | country: " + self.__pais + " | time: " + str(self.__tiempo)

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self, edad):
        self.__edad = edad

    @property
    def pais(self):
        return self.__pais

    @pais.setter
    def nombre(self, pais):
        self.__pais = pais

    @property
    def tiempo(self):
        return self.__tiempo

    @tiempo.setter
    def tiempo(self, tiempo):
        self.__tiempo = tiempo