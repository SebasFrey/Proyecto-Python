numero1 = int(input("Digite el primer número: "))
numero2 = int(input("Digite el segundo número: "))

if numero1 % 2 == 0 and numero2 % 2 == 0:
    print("Ambos números son pares")
elif numero1 % 2 == 0 and numero2 % 2 != 0:
    print(f"{numero1} es par")
elif numero1 % 2 != 0 and numero2 % 2 == 0:
    print(f"{numero2} es par")
else:
    print("Ambos números son impares")

