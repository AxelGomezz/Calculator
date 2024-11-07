#variables
num1 = 0
num2 = 0
op = ''

#Funciones
def sumar(num1,num2):
    print("Resultado : ",num1 + num2)

def restar(num1,num2):
    print("Resultado: ",num1 - num2)


print("Elegir operacion:\n[S]umar\n[R]estar: ")
op = input()


if op == 'S':
    num1 = int(input("--Suma--\nIngrese el numero: "))

    num2 = int(input("Ingrese el siguiente numero: "))

    sumar(num1,num2)