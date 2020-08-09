import math


def suma(num1, num2):
    resultado = []
    suma1 = round(num1[0] + num2[0])
    suma2 = round(num1[1] + num2[1])
    resultado = resultado + [suma1, suma2]
    return resultado


def resta(num1, num2):
    resultado = []
    resta1 = round(num1[0] - num2[0])
    resta2 = round(num1[1] - num2[1])
    resultado = resultado + [resta1, resta2]
    return resultado


def multi(num1, num2):
    resultado = []
    rest1 = round((num1[0] * num2[0]) - (num1[1] * num2[1]))
    rest2 = round((num1[0] * num2[1]) + (num1[1] * num2[0]))
    resultado = resultado + [rest1, rest2]
    return resultado


def division(num1, num2):
    resultado = []
    div1 = round(((num1[0] * num2[0]) + (num1[1] * num2[1])) / ((num2[0] ** 2) + (num2[1] ** 2)))
    div2 = round(((num1[1] * num2[0]) - (num1[0] * num2[1])) / ((num2[0] ** 2) + (num2[1] ** 2)))
    resultado = resultado + [div1, div2]
    return resultado


def modulo(num1):
    rta = round(((num1[0] ** 2) + (num1[1] ** 2))**(1/2),3)
    return rta


def conjugado(num1):
    rta = num1[1] * -1
    num1[1] = rta
    return num1


def polares(num1):
    resultado = []
    p = modulo(num1)
    theta = round(math.tan(num1[1] / num1[0]),3)
    resultado = resultado + [p, theta]
    return resultado


def cartesianos(num1):
    resultado = []
    a = round(num1[0] * (math.cos(num1[1])),3)
    b = round(num1[0] * (math.sin(num1[1])),3)
    resultado = resultado + [a, b]
    return resultado


def main():
    op = input(
        "Digite el simbolo o nombre de la operacion a realizar de las siguientes opciones:" + "\n" + "para sumar digite:  +" +
        "\n""para restar digite:  -" + "\n""para multiplicar digite=  *" + "\n""para dividir digite=  /" + "\n""para realizar el modulo digite=  modulo" +
        "\n""para realizar el conjugado digite=  conjugado" + "\n""para Conversión cartesiano a polar digite=  polares" + "\n""para Conversión polar a cartesiano digite=  cartesianos" + "\n")
    if op == "+":
        num1 = []
        num2 = []
        num1_1 = int(input("Digite el numero de la parte real del primer numero complejo"))
        num1_2 = int(input("Digite el numero de la parte imaginaria del primer numero complejo"))
        num2_1 = int(input("Digite el numero de la parte real del segundo numero complejo"))
        num2_2 = int(input("Digite el numero de la parte imaginaria del segundo numero complejo"))
        num1 = num1 + [num1_1, num1_2]
        num2 = num2 + [num2_1, num2_2]
        print(suma(num1, num2))
    elif op == "-":
        num1 = []
        num2 = []
        num1_1 = int(input("Digite el numero de la parte real del primer numero complejo"))
        num1_2 = int(input("Digite el numero de la parte imaginaria del primer numero complejo"))
        num2_1 = int(input("Digite el numero de la parte real del segundo numero complejo"))
        num2_2 = int(input("Digite el numero de la parte imaginaria del segundo numero complejo"))
        num1 = num1 + [num1_1, num1_2]
        num2 = num2 + [num2_1, num2_2]
        print(suma(num1, num2))
    elif op == "*":
        num1 = []
        num2 = []
        num1_1 = int(input("Digite el numero de la parte real del primer numero complejo"))
        num1_2 = int(input("Digite el numero de la parte imaginaria del primer numero complejo"))
        num2_1 = int(input("Digite el numero de la parte real del segundo numero complejo"))
        num2_2 = int(input("Digite el numero de la parte imaginaria del segundo numero complejo"))
        num1 = num1 + [num1_1, num1_2]
        num2 = num2 + [num2_1, num2_2]
        print(multi(num1, num2))
    elif op == "/":
        num1 = []
        num2 = []
        num1_1 = int(input("Digite el numero de la parte real del primer numero complejo"))
        num1_2 = int(input("Digite el numero de la parte imaginaria del primer numero complejo"))
        num2_1 = int(input("Digite el numero de la parte real del segundo numero complejo"))
        num2_2 = int(input("Digite el numero de la parte imaginaria del segundo numero complejo"))
        num1 = num1 + [num1_1, num1_2]
        num2 = num2 + [num2_1, num2_2]
        print(division(num1, num2))
    elif op == "modulo":
        num1 = []
        num1_1 = int(input("Digite el numero de la parte real del primer numero complejo"))
        num1_2 = int(input("Digite el numero de la parte imaginaria del primer numero complejo"))
        num1 = num1 + [num1_1, num1_2]
        print(modulo(num1))
    elif op == "conjugado":
        num1 = []
        num1_1 = int(input("Digite el numero de la parte real del primer numero complejo"))
        num1_2 = int(input("Digite el numero de la parte imaginaria del primer numero complejo"))
        num1 = num1 + [num1_1, num1_2]
        print(conjugado(num1))
    elif op == "polares":
        num1 = []
        num1_1 = int(input("Digite el numero de la parte real del primer numero complejo"))
        num1_2 = int(input("Digite el numero de la parte imaginaria del primer numero complejo"))
        num1 = num1 + [num1_1, num1_2]
        print(polares(num1))
    elif op == "cartesianos":
        num1 = []
        num1_1 = int(input("Digite el valor de rho"))
        num1_2 = int(input("Digite el angulo theta en grados"))
        num1_2=math.radians(num1_2)
        num1 = num1 + [num1_1, num1_2]
        print(cartesianos(num1))


main()
