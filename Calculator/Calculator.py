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


print("Elegir operacion:\n[S]umar\n[R]estar\n[M]ultiplicar\n[Dividir]: ")
operation = input()


if operation == 'S':#suma
    num1 = int(input("--Suma--\nIngrese el numero: "))
    num2 = int(input("Ingrese el siguiente numero: "))

    sumar(num1,num2)
elif operation == 'R':#resta
    num1 = int(input("--Resta--\nIngrese el numero: "))
    num2 = int(input("Ingrese el siguiente numero: "))

    restar(num1,num2)
elif operation == 'M':#multiplicacion
    num1 = int(input("--Multiplicar--\nIngrese el numero: "))
    num2 = int(input("Ingrese el siguiente numero: "))

    multiplicar(num1,num2)
elif operation == 'D':#division
    num1 = int(input("--Division--\nIngrese el numero: "))
    num2 = int(input("Ingrese el siguiente numero: "))

    division(num1,num2)