saldo=1000
def ver_saldo(saldo):
    print("\nTu saldo es ",saldo," pesos")
    input("presione enter para volver al menu anterior...")
def retirar(mont):
    a=saldo-mont
    print("\nTu nuevo saldo es: ",a)
    input("presione enter para volver al menu anterior...")
    return a
def depositar(mont):
    a=saldo+mont
    print("\nTu nuevo saldo es: ",a)
    input("presione enter para volver al menu anterior...")
    return a
def menu():
    print(        
    "________MENU_______\n\n",
    "Escoja una opcion:\n\n",
    "1) Consultar saldo\n",
    "2) Depositar dinero\n",
    "3) Retirar dinero\n",
    "4) Salir\n",
    "\n__________________"
)
while True:
    menu()
    while True:
        opcion=int(input("que opcion desea ejecutar: "))
        if opcion<1 or opcion > 4:
            print("ERROR\n Opcion ingresada invalida\n Vuelve a intentarlo")
            menu()
        else:
            break
    match opcion:
        case 1:
            ver_saldo(saldo)
        case 2:
            while True:
                monto=int(input("\nMonto a depositar: ")) #sumar a saldo
                if monto<0:
                    print("Valor invalido\nVuelve a intentarlo")
                else:
                    break
            saldo=depositar(monto) 
        case 3:
            while True:
                monto_retiro=int(input("\nIngresa el monto del retiro: "))
                if monto_retiro<0:
                    print("\nERROR valor invalido")
                elif monto_retiro>saldo:
                    print("\n ERROR SALDO INSUFICIENTE")
                else:
                    break
            saldo=retirar(monto_retiro)
        case 4:
            print("\nGracias por su visita\n\n")
            break