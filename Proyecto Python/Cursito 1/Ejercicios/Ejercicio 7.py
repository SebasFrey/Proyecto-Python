numero1 = int(input("Digite el primer número: "))
numero2 = int(input("Digite el segundo número: "))
numero3 = int(input("Digite el tercer número: "))

if numero1 >= numero2 and numero1 >= numero3:
    print(f"Número mayor es {numero1}")
elif numero2 >= numero1 and numero2 >= numero3:
    print(f"El numero mayor es {numero2}")
elif numero3 >= numero1 and numero3 >= numero2:
    print(f"El numero mayor es {numero3}")
