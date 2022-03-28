import numpy as np
#from Vectores_matrices import *


 from MATRIX-VECTOR-LIBRARY import *


def probability(pos, v):
    a = normVector(v[pos])
    b = normVector(v)
    probability = (a / b)
    return probability * 100


def VectorProduct(v, v1):
    answer = 0
    for i in range(len(v)):
        answer += v[i] * v1[i]
    return answer


""" Exercise # 4.3.1 """


def possibleProbability(posicion, index):
    states = [[(0, 1), (1, 0)], [(0, -1), (1, 0)], [(1, 0), (1, 0)], [(-1, 0), (1, 0)], [(0, 0), (1, 0)],
              [(1, 0), (0, 0)]]
    answer = []
    for i in range((index * 2) - 2, index * 2):
        if probability(posicion, states[i]) != 0.0:
            answer += states[i]
    return answer


""" Exercise # 4.3.2 """


def probabilityEigenValue(posicion, index):
    matrices = [[[(1, 0), (0, 0)], [(0, 0), (-1, 0)]], [[(0, 0), (0, -1)], [(0, 1), (0, 0)]],
                [[(0, 0), (1, 0)], [(1, 0), (0, 0)]]]
    valoresPropios, probabilityAux = [], []
    aux = possibleProbability(posicion, index)
    answer = 0
    for i in range(3):
        values, no = np.linalg.eig(matrices[i])
        valoresPropios += values

    for j in range(len(aux)):
        probabilityAux += probability(posicion, aux[j])

    for k in range(2):
        answer += (probability[i] * valoresPropios[indice][k])

    return answer


""" Exercise # 4.4.1"""


def verificarUnitarias(u1, u):
    if unitMatrix(m)(U1) and unitMatrix(m)(u):
        answer = matrixProduct(u1, u)
        return unitMatrix(answer)


""" Exercise # 4.4.2 """


def ExperimentoCanicas(v, n, clicks):
    for i in range(clicks):
        v = multiScalarMatrixCplx(v, n)
    return v
