# Definimos las variables
a = 20
b = 23
c = 25

# 1. print(): Imprime los valores en la consola.
print("Valores de a, b y c:")
print("a =", a)  # 20
print("b =", b)  # 23
print("c =", c)  # 25

# 2. type(): Devuelve el tipo de la variable.
print("\nTipo de las variables:")
print("Tipo de a:", type(a))  # <class 'int'>
print("Tipo de b:", type(b))  # <class 'int'>
print("Tipo de c:", type(c))  # <class 'int'>

# 3. abs(): Devuelve el valor absoluto.
print("\nValor absoluto de la diferencia entre a y b:")
print("abs(a - b):", abs(a - b))  # 3

# 4. max() y min(): Devuelven el valor máximo y mínimo, respectivamente.
print("\nMáximo y mínimo de a, b y c:")
print("max(a, b, c):", max(a, b, c))  # 25
print("min(a, b, c):", min(a, b, c))  # 20

# 5. sum(): Devuelve la suma de un iterable.
print("\nSuma de a, b y c:")
print("sum([a, b, c]):", sum([a, b, c]))  # 68

# 6. pow(): Eleva un número a la potencia de otro.
print("\nPotencia de a al cuadrado:")
print("pow(a, 2):", pow(a, 2))  # 400

# 7. divmod(): Devuelve el cociente y el resto de la división.
print("\nDivisión de c entre b usando divmod:")
cociente, resto = divmod(c, b)
print("divmod(c, b): cociente =", cociente, ", resto =", resto)  # (1, 2)

# 8. round(): Redondea un número al entero más cercano.
print("\nRedondeo de c dividido por b a 2 decimales:")
print("round(c / b, 2):", round(c / b, 2))  # 1.09

# 9. sorted(): Devuelve una lista ordenada.
print("\nLista ordenada de a, b y c:")
print("sorted([b, c, a]):", sorted([b, c, a]))  # [20, 23, 25]

# 10. len(): Devuelve la longitud de un iterable.
lista = [a, b, c]
print("\nLongitud de la lista [a, b, c]:")
print("len(lista):", len(lista))  # 3
