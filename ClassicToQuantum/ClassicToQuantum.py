import new_complejos
import numpy as np
import matplotlib.pyplot as plt
import scipy
from new_complejos import *


def actionbool(mat, vect):
    fil, col = len(mat), len(mat[0])
    len_vect = len(vect)
    if col == len_vect:
        rta = [False for k in range(fil)]
        for i in range(fil):
            boolean = True
            for j in range(col):
                boolean = mat[i][j] and vect[j]
                rta[i] = rta[i] or boolean
        return rta
    else:
        return "Length error"


def action(mat, vect):
    if len(mat[0]) == len(vect):
        vector = [0 for i in range(len(vect))]
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                vector[i] = (vector[i] + (mat[i][j] * vect[j]))
        return vector
    else:
        return "Length error"


def experimentBool(mat, vect, clicks):
    for j in range(clicks):
        new_vect = actionbool(mat, vect)
        vect = new_vect
    return vect


def matriz_reales(mat, vect, clicks):
    for j in range(clicks):
        new_vect = action(mat, vect)
        vect = new_vect
    return vect


def action_complex(mat, vect):
    if len(mat[0]) == len(vect):
        vector = [(0, 0) for i in range(len(vect))]
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                vector[i] = suma(vector[i], multi(mat[i][j], vect[j]))
        return vector
    else:
        return "Length error"


def matriz_complex(mat, vect, clicks):
    resultado = [(0, 0) for x in range(len(vect))]
    for j in range(clicks):
        new_vect = action_complex(mat, vect)
        vect = new_vect
    if vect != "Length error":
        for i in range(len(vect)):
            num = modulo(vect[i]) ** 2
            resultado[i] = num
    else:
        resultado = "Length error"
    return resultado


def grafica(mat, vect, clicks):
    posiciones = [number for number in range(len(vect))]
    probability = matriz_complex(mat, vect, clicks)
    fig, ax = plt.subplots()
    ax.set_ylabel('Probability')
    ax.set_xlabel('Position')
    ax.set_title('Quantum system probability')
    plt.bar(posiciones, probability)
    plt.savefig('Quantum_system_probability.png')
    plt.show()