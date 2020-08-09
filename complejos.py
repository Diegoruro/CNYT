import math


def suma(num1, num2):
    resultado = []
    suma1 = round(num1[0] + num2[0],3)
    suma2 = round(num1[1] + num2[1],3)
    resultado = resultado + [suma1, suma2]
    return resultado


def resta(num1, num2):
    resultado = []
    resta1 = round(num1[0] - num2[0],3)
    resta2 = round(num1[1] - num2[1],3)
    resultado = resultado + [resta1, resta2]
    return resultado


def multi(num1, num2):
    resultado = []
    rest1 = round((num1[0] * num2[0]) - (num1[1] * num2[1]),3)
    rest2 = round((num1[0] * num2[1]) + (num1[1] * num2[0]),3)
    resultado = resultado + [rest1, rest2]
    return resultado


def division(num1, num2):
    resultado = []
    div1 = round(((num1[0] * num2[0]) + (num1[1] * num2[1])) / ((num2[0] ** 2) + (num2[1] ** 2)),3)
    div2 = round(((num1[1] * num2[0]) - (num1[0] * num2[1])) / ((num2[0] ** 2) + (num2[1] ** 2)),3)
    resultado = resultado + [div1, div2]
    return resultado


def modulo(num1):
    rta = round(((num1[0] ** 2) + (num1[1] ** 2)) ** (1 / 2), 3)
    return rta


def conjugado(num1):
    rta = num1[1] * -1
    num1[1] = rta
    return num1


def polares(num1):
    resultado = []
    p = modulo(num1)
    theta = round(math.atan(num1[1] / num1[0]), 3)
    resultado = resultado + [p, theta]
    return resultado


def cartesianos(num1):
    resultado = []
    a = round(num1[0] * (math.cos(num1[1])), 3)
    b = round(num1[0] * (math.sin(num1[1])), 3)
    resultado = resultado + [a, b]
    return resultado


def fase(num1):
    fase1 = round(math.atan(num1[1] / num1[0]), 3)
    return fase1