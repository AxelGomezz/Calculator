#variables
num1 = 0
num2 = 0
operation = ''

#Funciones suma y resta
def sumar(num1,num2):
    print("Resultado : ",num1 + num2)

def restar(num1,num2):
    print("Resultado: ",num1 - num2)

#Funciones multiplicacion y division
def multiplicar(num1, num2):
    print("Resultado: ",num1 * num2)

def division(num1, num2):
    print("Resultado: ",num1 / num2)

#Solicita datos al usuario
def pedirNum():
    while True:
        try:
            num1 = int(input("\nIngrese el numero: "))
            num2 = int(input("\nIngrese el siguiente numero: "))
            return num1,num2
            break
        except ValueError:
            print("Error: Porfavor ingrese un numero entero.")

print("Elegir operacion:\n[S]umar\n[R]estar\n[M]ultiplicar\n[D]ividir: ")
operation = input()


if operation == 'S':#suma
    print("--Suma--\n")
    num1, num2 = pedirNum()
    sumar(num1,num2)
elif operation == 'R':#resta
    print("--Resta--\n")
    num1, num2 = pedirNum()
    restar(num1,num2)
elif operation == 'M':#multiplicacion
    print("--Multiplicacion--\n")
    num1, num2 = pedirNum()
    multiplicar(num1,num2)
elif operation == 'D':#division
    print("--Division--\nIngrese el numero: ")
    num1, num2 = pedirNum()
    division(num1,num2)