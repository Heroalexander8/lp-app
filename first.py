<<<<<<< HEAD


# clase obrero

class Obrero:
    def __init__(self, nombre, edad, peso, talla):
        self.nombre = nombre
        self.edad = edad
        self.peso = peso
        self.talla = talla

    def imc(self):
        imc = self.peso / (self.talla)**2
        if imc < 18.5:
            return ("Bajo peso", imc)
        elif imc >= 18.5 and imc < 24.9:
            return ("Normal", imc)
        elif imc >= 25 and imc <= 29.9:
            return ("Sobrepeso", imc)
        elif imc >= 30:
            return ("Obesidad", imc)


init = Obrero("Juan", 30, 70, 1.70)
print(init.nombre, "cuya edad es", init.edad,
      "tiene un imc determinado como -> ", init.imc())
=======
nombre = "Carlos"
edad = 22
matricul = True
print("prueba")
>>>>>>> 2064b6d6f49a9596605c0c06a4113c963b1d28ef
