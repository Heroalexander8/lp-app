# realice una app que divida dos numeros con try y except

def division(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "No se puede dividir por cero"
    except TypeError:
        return "Solo se pueden dividir numeros"
    except ValueError:
        return "Solo se pueden dividir numeros"


a = print(input("Ingrese el primer numero: "))
b = print(input("Ingrese el segundo numero: "))
print(division(a, b))
