num1 = float(input("Digite un numero: "))
num2 = float(input("Digite un numero: "))
operacion = input("Digite una operacion: ")

if operacion == "S":
    suma = num1 + num2
    print(f"\nLa suma es: {suma}")
elif operacion == "R":
    resta = num1 - num2
    print(f"\nLa resta es: {resta}")
elif operacion == "M" or operacion == "P":
    multi = num1 * num2
    print(f"\nLa multiplicacion es: {multi}")
elif operacion == "D":
    division = num1 / num2
    print(f"\nLa division es: {division}")
else:
    print(f"Estas Pendejo O Que Hijo?")
