# Solicitar al usuario que ingrese el valor de a y convertirlo a entero
a = int(input("a ->"))

# Solicitar al usuario que ingrese el valor de b y convertirlo a entero
b = int(input("b ->"))

# Intercambiar los valores de a y b utilizando una variable temporal, pero tambien se puede. a, b=b,a.
intercambio = a
a = b
b = intercambio

# Imprimir los valores intercambiados
print(f"Ahora a es: {a}")
print(f"Ahora b es: {b}")
