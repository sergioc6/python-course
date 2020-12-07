#Ejercicio 1

a = float(input("Ingrese el valor de a: "))
b = float(input("Ingrese el valor de b: "))
c = float(input("Ingrese el valor de c: "))

result = (pow(a, 3) * (pow(b, 2) - (2 * a * c))) / (2*b)

print(f"El resultado es: {result}")
