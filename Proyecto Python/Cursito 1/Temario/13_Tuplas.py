# Tupla con los nuevos valores
tupla_1 = (
    4,
    "hola",
    6.78,
    [1, 2, 3],
    4,
)

# Tupla inicial (tuplas no tienen método append)
tupla_2 = (4, "hola", 6.78, [1, 2, 3], 4)
# Concatenación para agregar elementos
tupla_2 = tupla_2 + (5,)

# Tupla con un nuevo elemento insertado (creando una nueva tupla)
tupla_3 = (4, "hola", 6.78, [1, 2, 3], 4)
tupla_3 = tupla_3[:2] + (7,) + tupla_3[2:]

# Tupla extendida (creando una nueva tupla)
tupla_4 = (4, "hola", 6.78, [1, 2, 3], 4)
tupla_4 = tupla_4 + (5, 6.78, "mundo")

# Concatenación de tuplas
tupla_5 = tupla_4 + tupla_3

# Mostramos la longitud de tupla_1
print("Longitud de tupla_1:", len(tupla_1))

# Imprimimos tupla_2
print("tupla_2:", tupla_2)

# Imprimimos tupla_3
print("tupla_3:", tupla_3)

# Imprimimos tupla_4
print("tupla_4:", tupla_4)

# Imprimimos tupla_5
print("tupla_5:", tupla_5)

# Verificamos si "hola" está en tupla_1
print('"hola" en tupla_1:', "hola" in tupla_1)

# Imprimimos el índice de "hola" en tupla_1
print('Índice de "hola":', tupla_1.index("hola"))

# Contamos cuántas veces aparece el número 4 en tupla_6
tupla_6 = (4, "hola", 6.78, [1, 2, 3], 4)
print("Número 4 en tupla_6:", tupla_6.count(4))

# Tupla vacía (creando una nueva tupla)
tupla_7 = (4, "hola", 6.78, [1, 2, 3], 4)
tupla_7 = ()

print("tupla_7 después de vaciarla:", tupla_7)

# Tupla invertida (creando una nueva tupla)
tupla_8 = (4, "hola", 6.78, [1, 2, 3], 4)
tupla_8 = tupla_8[::-1]
print("tupla_8 invertida:", tupla_8)

# Tupla duplicada
tupla_9 = (4, "hola", 6.78, [1, 2, 3], 4) * 2
print("tupla_9 duplicada:", tupla_9)

# Ordenar tupla (las tuplas contienen diferentes tipos de datos, no se puede ordenar)
# Para fines demostrativos, omitimos esta parte ya que `sorted()` no funciona con tuplas heterogéneas.
