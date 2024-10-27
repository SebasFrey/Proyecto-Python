saldo_incial = 1000
print("\t. :MENU:.")
print("1. Ingresar Dineros A La Cuenta")
print("2. Retirar Dineros De La Cuenta")
print("3. Mostrar Dineros Disponible")
print("4.Salir")
opciones = int(input("Digite Una Opcion De Menu: "))
print()
if opciones == 1:
    extra = float(input("Cuanto Dinero Desea Ingresar"))
    saldo_incial = saldo_incial + extra
    print(f"El Dinero disponible es de : {saldo_incial}")

    
