# Lista con diferentes tipos de elementos
lista_1 = [
    "Lunes",
    "Martes",
    "Miércoles",  # Corrección ortográfica
    "Jueves",
    "Viernes",
    20,
    9.36,
    [1, 2, 3],
    True,
]

# Lista inicial
lista_2 = [1, 2, 3, 4, 5]

# Agregamos un elemento al final
lista_2.append(6)

# Lista con un nuevo elemento insertado en la posición 2
lista_3 = [1, 2, 4, 5]
lista_3.insert(2, 3)

# Lista extendida con más elementos
lista_4 = [1, 2, 3, 4, 5]
lista_4.extend([6, 7, 8])

# Concatenación de listas
lista_5 = lista_4 + lista_3

# Mostramos la longitud de lista_1
print("Longitud de lista_1:", len(lista_1))

# Imprimimos lista_2
print("lista_2:", lista_2)

# Imprimimos lista_3
print("lista_3:", lista_3)

# Imprimimos lista_4
print("lista_4:", lista_4)

# Imprimimos lista_5
print("lista_5:", lista_5)

# Verificamos si "Lunes" está en lista_1
print('"Lunes" en lista_1:', "Lunes" in lista_1)

# Imprimimos el índice de "Lunes" en lista_1
print('Índice de "Lunes":', lista_1.index("Lunes"))

# Contamos cuántas veces aparece el número 25 en lista_6
lista_6 = [20, 23, 23, 20, 25, 18]
print("Número 25 en lista_6:", lista_6.count(25))

# Limpiamos lista_7
lista_7 = [20, 23, 23, 20, 25, 18]
lista_7.clear()
print("lista_7 después de clear:", lista_7)

# Invertimos el orden de lista_8
lista_8 = [20, 23, 23, 20, 25, 18]
lista_8.reverse()
print("lista_8 invertida:", lista_8)

# Multiplicamos lista_9 por 2
lista_9 = [20, 23, 23, 20, 25, 18] * 2
print("lista_9 duplicada:", lista_9)

# Ordenamos lista_10 en orden ascendente
lista_10 = [20, 23, 23, 20, 25, 18]
lista_10.sort()
print("lista_10 ordenada ascendente:", lista_10)

# Ordenamos lista_11 en orden descendente
lista_11 = [20, 23, 23, 20, 25, 18]
lista_11.sort(reverse=True)
print("lista_11 ordenada descendente:", lista_11)
