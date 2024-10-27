a = 20
b = 23
c = 25

# Ejemplo 1
resultado1 = (a < b) and (b < c)
print(resultado1)  # True porque 20 < 23 y 23 < 25

# Ejemplo 2
resultado2 = (a > b) and (b < c)
print(resultado2)  # False porque 20 no es mayor que 23 aunque 23 < 25


# Ejemplo 1
resultado3 = (a < b) or (b > c)
print(resultado3)  # True porque 20 < 23 aunque 23 no es mayor que 25

# Ejemplo 2
resultado4 = (a > b) or (b > c)
print(resultado4)  # False porque 20 no es mayor que 23 y 23 no es mayor que 25


# Ejemplo 1
resultado5 = not (a < b)
print(resultado5)  # False porque 20 < 23 y el operador not invierte el valor

# Ejemplo 2
resultado6 = not (b > c)
print(resultado6) # True porque 23 no es mayor que 25 y el operador not invierte el valor
