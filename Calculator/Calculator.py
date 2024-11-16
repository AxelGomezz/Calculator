#variables
num1 = 0
num2 = 0
operation = ''
resultado = 0

#Funciones suma y resta
def sumar(num1,num2):
    return num1 + num2

def restar(num1,num2):
    return num1 - num2

#Funciones multiplicacion y division
def multiplicar(num1, num2):
    return num1 * num2

def division(num1, num2):
    while 0 in (num1,num2):
        print("\nNo se puede dividir por cero! Porfavor ingrese otro numero")
        num1,num2 = pedirNum()
    return num1 / num2


#Solicita datos al usuario
def pedirNum():
    while True:
        try:
            num1 = int(input("Ingrese el numero: "))
            num2 = int(input("Ingrese el siguiente numero: "))
            return num1,num2
            break
        except ValueError:
            print("Error: Porfavor ingrese un numero entero.")


#Solicita accion a realizar.
def chooseOperation():
    operation = ''
    while True:
            operation = input("\nElegir operacion:\n[S]umar\n[R]estar\n[M]ultiplicar\n[D]ividir: ")
            operation = operation.upper()
            if operation in ['S','R','M','D']:
                break
            else:
                print("\nError: Porfavor ingrese una opcion valida.")
    return operation


#MAIN
operation = chooseOperation()

if operation  == 'S':#suma
    print("\n--Suma--")
    num1, num2 = pedirNum()
    resultado = sumar(num1,num2)
    print("El resultado es:",resultado)

elif operation == 'R':#resta
    print("\n--Resta--")
    num1, num2 = pedirNum()
    resultado = restar(num1,num2)
    print("El resultado es:",resultado)

elif operation == 'M':#multiplicacion
    print("\n--Multiplicacion--")
    num1, num2 = pedirNum()
    resultado = multiplicar(num1,num2)
    print("El resultado es:",resultado)

elif operation == 'D':#division
    print("\n--Division--")
    num1, num2 = pedirNum()
    resultado = division(num1,num2)
    print("El resultado es:",resultado)