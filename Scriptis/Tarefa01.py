# -*- coding: utf-8 -*-
"""
Este script foi criado para a execução da Tarefa 01. 

- Criar uma matriz com números aleatórios com duas dimensões 
(2D) com 100 linhas e 100 colunas.
- Recortar a primeira linha e listar os valores
- Determinar o valor da última linha e coluna

"""
#Importando numpy
import numpy as np

# Criando a matriz
X = np.random.rand(100, 100) 

#Recortando a primeira linha e listar os valores
linha1 = X[0, :]
print("Valores da primeira linha:")
print(linha1)

# Deterinar o valor da última linha e coluna
xfinal = X[-1, -1]
print("Valor da última linha e coluna:")
print(xfinal)

# Fim da tarefa