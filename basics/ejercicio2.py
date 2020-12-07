# Ejercicio 2

a = float(input("Ingrese el valor de a: "))
b = float(input("Ingrese el valor de b: "))

first = (3 + 5 * 8) < 3
second = ((-(6 / 3) * 4) + 2) < 2
third = (a > b)

result = first and second or third

print(f"El resultado es: {result}")
