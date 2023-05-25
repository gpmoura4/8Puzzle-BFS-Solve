class Node:
    # construtor
    def __init__(self, state, cost, action=None, father=None):
        self.state = state
        self.cost = cost
        self.father = father
        self.action = action
        if father is None:
            self.caminho = []
            # print('nó inicial')
        else:
            self.caminho = []
            # print('caminho sendo adicionado')
            self.caminho.append(self.action)
            self.caminho.extend(self.father.caminho)
            # print(self.caminho)


import copy
import time
import psutil
import queue
from collections import deque
from typing import Deque, Any


matrizOriginal = [[0, 8, 7], [6, 5, 4], [3, 2, 1]]


matrizFinal = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]


# Procurando o Zero
def searchZero(matrizOriginal):
    for i in range(len(matrizOriginal)):
        for j in range(len(matrizOriginal[0])):
            if matrizOriginal[i][j] == 0:
                return i, j


def comparar_matrizes(currentMatriz, finalMatriz):
    if len(currentMatriz) != len(finalMatriz) or len(currentMatriz[0]) != len(
        finalMatriz[0]
    ):
        return False  # se as matrizes tiverem tamanhos diferentes, elas não são iguais

    for i in range(len(currentMatriz)):
        for j in range(len(currentMatriz[0])):
            if currentMatriz[i][j] != finalMatriz[i][j]:
                return False  # se um elemento for diferente, as matrizes não são iguais

    return True  # se todas as comparações forem iguais, as matrizes são iguais


# transforma um tupla


def turnInTuple(matriz):
    matrizTuple = tuple(tuple(linha) for linha in matriz)
    return matrizTuple


def turnInString(matriz):
    matrizStr = "".join(str(i) for j in matriz for i in j)
    return matrizStr


# Gera estados a partir de uma possivel ação


def geraEstados(matrizOriginal):
    posicoesPossiveis = {
        (0, 0): ["Right", "Down"],
        (0, 1): ["Right", "Down", "Left"],
        (0, 2): ["Left", "Down"],
        (1, 0): ["Up", "Righ", "Down"],
        (1, 1): ["Left", "Up", "Right", "Down"],
        (1, 2): ["Up", "Left", "Down"],
        (2, 0): ["Up", "Right"],
        (2, 1): ["Left", "Up", "Right"],
        (2, 2): ["Left", "Up"],
    }

    # Achando qual as posiçoes possiveis para um posicionamento especifico
    # index do zero
    index = searchZero(matrizOriginal)
    # Vetor com as posições possiveis (Right...Down)
    chavePosicional = posicoesPossiveis[searchZero(matrizOriginal)]
    # vetor com os estados de cada nó
    nodeStates = []

    # For das possibilidades de estados
    for movimento in chavePosicional:
        # COPIA MATRIZ
        matrizCopia = copy.deepcopy(matrizOriginal)

        if movimento == "Right":
            currentState = trocaDireita(matrizCopia, index)

        if movimento == "Left":
            currentState = trocaEsquerda(matrizCopia, index)

        if movimento == "Up":
            currentState = trocaCima(matrizCopia, index)

        if movimento == "Down":
            currentState = trocaBaixo(matrizCopia, index)

        # Salva estado e movimento
        nodeStates.append((currentState, movimento))

    return nodeStates


def trocaDireita(matrizCopia, index):
    # trocando as posicoes
    # matrizCopia [ index[0] ] [ index[1] ], matrizCopia[ index[0] ] [ index[1] + 1] = matrizCopia[index[0]][index[1] + 1], matrizCopia[index[0]][index[1]]

    matrizCopia[index[0]][index[1]], matrizCopia[index[0]][index[1] + 1] = (
        matrizCopia[index[0]][index[1] + 1],
        matrizCopia[index[0]][index[1]],
    )

    return matrizCopia


def trocaEsquerda(matrizCopia, index):
    # trocando as posicoes
    matrizCopia[index[0]][index[1]], matrizCopia[index[0]][index[1] - 1] = (
        matrizCopia[index[0]][index[1] - 1],
        matrizCopia[index[0]][index[1]],
    )
    return matrizCopia


def trocaCima(matrizCopia, index):
    # trocando as posicoes
    matrizCopia[index[0]][index[1]], matrizCopia[index[0] - 1][index[1]] = (
        matrizCopia[index[0] - 1][index[1]],
        matrizCopia[index[0]][index[1]],
    )

    return matrizCopia


def trocaBaixo(matrizCopia, index):
    # trocando as posicoes
    matrizCopia[index[0]][index[1]], matrizCopia[index[0] + 1][index[1]] = (
        matrizCopia[index[0] + 1][index[1]],
        matrizCopia[index[0]][index[1]],
    )
    return matrizCopia


# BFS
def BFS(matrizOriginal):
    startTime = time.time()
    startMemory = psutil.Process().memory_info().rss

    initialNode = Node(matrizOriginal, 0)

    if comparar_matrizes(initialNode.state, matrizFinal):
        print("achei solução")
        return initialNode
    # fim if

    caminho = []

    # Criando a fila
    borda = queue.Queue()
    borda.put(initialNode)

    # conjuntando de nós explorados
    explorado = set()
    # transformando a matriz em string
    matrizStr = turnInString(initialNode.state)
    # adicionando elemento ao conjunto dos explorados
    explorado.add(matrizStr)

    # Contador para os nós expandidos
    noExpandido = 0
    # Fringe Size
    fringeNode = 0
    # Max Fringe Size
    max_search_depth = 0

    while not borda.empty():
        # Fringe Size contador
        fringeNode = fringeNode + 1
        noDesenfilado = borda.get()
        # max_search_depth = max(max_search_depth, noDesenfilado.cost)

        # Transformando o no desenfilado em string
        noDesenfiladoStr = turnInString(noDesenfilado.state)
        if noDesenfiladoStr not in explorado:
            noExpandido = noExpandido + 1
        # fim if

        # print(type(noDesenfilado.state))
        # Adicionando aos elementos explorados
        explorado.add(noDesenfiladoStr)

        # vetor de estados de cada nó + movimentação
        vetorEstados = geraEstados(noDesenfilado.state)
        # print(vetorEstados)

        # value --> valor na posicao atual
        #       0               1       2
        # (estado,movimento)
        #  value[0], value[1]
        for value in vetorEstados:
            # print(value)
            currentNode = Node(
                value[0], noDesenfilado.cost + 1, value[1], noDesenfilado
            )

            # guardando os movimentos
            caminho.append(currentNode.action)

            # print('NÓ ATUAL')
            # print(currentNode.state)

            # Transformando o no atual em string
            currentNodeStr = turnInString(currentNode.state)

            if currentNodeStr not in explorado:
                # Compare se o estado atual do current node é igual a solução
                if comparar_matrizes(currentNode.state, matrizFinal):
                    endTime = time.time()
                    duration = endTime - startTime
                    endMemory = psutil.Process().memory_info().rss
                    maxRamUsage = endMemory - startMemory
                    max_search_depth = max(max_search_depth, currentNode.cost)
                    return (
                        currentNode,
                        noExpandido,
                        fringeNode,
                        max_search_depth,
                        duration,
                        maxRamUsage,
                    )
                # Adicionando um novo filho na fila
                borda.put(currentNode)

        # fim for
    # fim while
    return None


answer = BFS(matrizOriginal)
print("O estado do no final eh: ", answer[0].state)
print("O caminho eh: ", answer[0].caminho)
print("O custo eh: ", answer[0].cost)
print("Os nos expandidos sao: ", answer[1])
print("O fringe size eh: ", answer[2])
print("O search depth eh: ", answer[0].cost)
print("O search depth maximo eh: ", answer[3])
print("O tempo de execucao foi de: ", answer[4])
print("A memoria ram utilizada foi: ", answer[5])
