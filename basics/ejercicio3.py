#Ejercicio 3

a = float(input("Ingrese el valor de a: "))

b = float(input("Ingrese el valor de b: "))

print(f"a(inicial)= {a}")
print(f"b(inicial)= {b}")

c = a
a = b
b = c

print(f"a(actual)= {a}")
print(f"b(actual)= {b}")
