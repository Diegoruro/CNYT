import math


def suma(num1, num2):
    suma1 =num1[0] + num2[0]
    suma2 =num1[1] + num2[1]
    resultado = suma1, suma2
    return resultado


def resta(num1, num2):
    resta1 = round(num1[0] - num2[0], 3)
    resta2 = round(num1[1] - num2[1], 3)
    resultado = resta1, resta2
    return resultado


def multi(num1, num2):
    rest1 = (num1[0] * num2[0]) - (num1[1] * num2[1])
    rest2 = (num1[0] * num2[1]) + (num1[1] * num2[0])
    resultado = rest1, rest2
    return resultado


def division(num1, num2):
    div1 = round(((num1[0] * num2[0]) + (num1[1] * num2[1])) / ((num2[0] ** 2) + (num2[1] ** 2)), 3)
    div2 = round(((num1[1] * num2[0]) - (num1[0] * num2[1])) / ((num2[0] ** 2) + (num2[1] ** 2)), 3)
    resultado = div1, div2
    return resultado


def modulo(num1):
    rta = round(((num1[0] ** 2) + (num1[1] ** 2)) ** (1 / 2), 2)
    return rta


def conjugado(num1):
    img = num1[1] * -1
    rta = num1[0], img
    return rta


def polares(num1):
    p = modulo(num1)
    theta = round(math.atan2(num1[1] , num1[0]), 3)
    resultado = p, theta
    return resultado


def cartesianos(num1):
    a = round(num1[0] * (math.cos(num1[1])), 3)
    b = round(num1[0] * (math.sin(num1[1])), 3)
    resultado = a, b
    return resultado


def fase(num1):
    fase1 = round(math.atan2(num1[1], num1[0]), 3)
    return fase1


def suma_vecto(vect1, vect2):
    resultado = []
    if len(vect1) != len(vect1):
        print("Error: diferent lenght vectors")
    for i in range(len(vect1)):
        suma_real = suma(vect1[i], vect2[i])
        resultado += [suma_real]
    return resultado


def inverse(num):
    num2 = num[0] * -1, num[1] * -1
    return num2


def inverse_vecto(vect):
    for i in range(len(vect)):
        vect[i] = inverse(vect[i])
    return vect


def multi_esc(num, vect):
    resultado = []
    for i in range(len(vect)):
        multi_vect = multi(num, vect[i])
        resultado += [multi_vect]
    return resultado


def suma_mat(mat1, mat2):
    resultado = []
    for i in range(len(mat1)):
        suma = suma_vecto(mat1[i], mat2[i])
        resultado += [suma]
    return resultado


def inverse_mat(mat):
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            mat[i][j] = inverse(mat[i][j])
    return mat


def multi_esc_mat(num, mat):
    resultado = []
    for i in range(len(mat)):
        mult = multi_esc(num, mat[i])
        resultado += [mult]
    return resultado


def traspuesta(vect):
    n = len(vect)  # filas
    m = len(vect[0])  # columnas
    matriz = [[0 for i in range(n)] for j in range(m)]
    for i in range(n):
        for j in range(m):
            matriz[j][i] = vect[i][j]
    return matriz


def conjugada_mat(mat):
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            mat[i][j] = conjugado(mat[i][j])
    return mat


def adjunta(mat):
    mat2 = [[mat[i][j] for j in range(len(mat[0]))] for i in range(len(mat))]
    mat2 = conjugada_mat(mat2)
    mat2 = traspuesta(mat2)
    return mat2


def producto(mat1, mat2):
    if len(mat1[0]) != len(mat2):
        return "Is not possible"
    else:
        matriz = [[(0, 0) for i in range(len(mat2[0]))] for j in range(len(mat1))]
        for i in range(len(mat1)):
            for j in range(len(mat2[0])):
                for k in range(len(mat1[0])):
                    matriz[i][j] = suma(matriz[i][j], multi(mat1[i][k], mat2[k][j]))
    return matriz


def Accion(mat, vect):
    rta = producto(mat, vect)
    return rta


def product_int(vect1, vect2):
    if isinstance(vect1[0], tuple) or isinstance(vect2[0], tuple):
        rta = (0, 0)
        if len(vect1) == len(vect2):
            for i in range(len(vect1)):
                rta = suma(rta, (multi(vect1[i], vect2[i])))
        return rta
    else:
        vect = adjunta(vect1)
        rta = producto(vect, vect2)
        return rta[0][0]


def norma(vect):
    suma = 0
    for i in range(len(vect)):
        suma += (modulo(vect[i]) ** 2)
    return round(suma ** (1 / 2), 2)


def distancia(vect1, vect2):
    resultado = []
    if len(vect1) != len(vect1):
        print("Error: diferent lenght vectors")
    else:
        for i in range(len(vect1)):
            resta_vect = resta(vect1[i], vect2[i])
            resultado += [resta_vect]
    return abs(norma(resultado))


def unit(mat):
    if len(mat) == len(mat[0]):
        In = [[(0, 0) for j in range(len(mat[0]))] for i in range(len(mat))]
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if i == j:
                    In[i][j] = (1, 0)
        mat1 = adjunta(mat)
        product = producto(mat1, mat)
        rta = True
        for i in range(len(mat)):
            for j in range(len(mat)):
                if product[i][j] != In[i][j]:
                    rta = False
        if rta:
            return True
        else:
            return False
    else:
        return "The input have to be a square matrix"


def herm(mat):
    aux = mat[:]
    mat2 = adjunta(aux)
    rta = True
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] == mat2[i][j] and mat[i][j] == mat2[i][j]:
                continue
            else:
                rta = False
    return rta


def tensor(mat1, mat2):
    for i in range(len(mat1)):
        for j in range(len(mat2)):
            h = mat1[i][j]
            mat1[i][j] = multi_esc_mat(h, mat2)
    return mat1


def printmatrix(matrix):
    for row in range(len(matrix)):
        print(''.join(map(str, matrix[row])))
