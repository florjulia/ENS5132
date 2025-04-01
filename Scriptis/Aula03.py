# -*- coding: utf-8 -*-
"""
Este script foi criado na terceira aula da disciplina ENS5132. Nesta aula, trablharemos com: 
    - Arrays numpy
    - Panda Dataforme
    - Matplotlib
    
    * requisitos: pip install spyder numpy pandas matplotlib

"""

#%% Importação de pacotes 

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#%% Relembrando listas

#  Criando uma lista com inteiros, string e float
listA = [1, 2, 3, 'teste', 20.5]
print(listA)

#criando uma lista com inteitos e float
listB = (1, 2, 3, 20.5)
print(listB)
#%% Trabalhando com numpy[]

# criando um array numpy 

arr = np.array([0.7, 0.75, 1.85])

#criando um array numpy a partir de uma lista 
arr2 = np.array(listA)

#criando um array numpy a partir de uma lista com números
arr3 = np.array(listB)

# Criando uma matriz 
precip = np.array([[1.07, 0.44, 1.50],[0.27, 1.33, 1.72]])

# Acessando o valor da primeira linha e coluna

print(precip[0,0])

# Acessando todos os valores da primeira linha 

print (precip[0,:])

# Acessando todos os valores da primeita coluna 
print (precip[:,0])
precipSlice = precip [:,0]

# Extraindo os dois primeiros valores da primeira linha
print(precip[0,0:1])

# Extraindo o último valor da última coluna 
print (precip [-1,-1])

#-------------------------------------------------------------------------------
# Criando matrizes com múltiplas dimensões 

# Criando um arranjo de dados com ínicio, fim e passo
x = np.arange(1,16,1)

# Mudando o shape/dimensão da matriz
xReshape = x.reshape(3,5)

# Transposta
print(xReshape.transpose())

# Criando uma matriz de núemros aleatórios
matRand = np.random.rand(10, 100, 100)

# Recortando matriz
matRandSlice = matRand[0,:,:]

# Criando matriz com 4D
matRand4D = np.random.rand(3, 10, 100, 100)

# Dimensão da matriz
print(matRand4D.ndim)

# Shape da matriz
print(matRand4D.shape)

# Número de elementos 
print (matRand4D.size)

# Múltiplicação 
print(matRand4D*3.9)

# Abrir dados de um arquivo de textos
dataSample = np.loadtxt(r"E:\UFSC 2025\Dados\teste1.txt")

# Abrir arquivo com formato separado por vírgula .csv
dataSample2 = np.loadtxt(r"E:\UFSC 2025\Dados\teste2.txt", 
                         delimiter=',')

# Média da matriz4D
print(matRand4D.mean()) 

# Média da matriz inteira 
print (matRand4D.max(axis=0))
matRand4D = matRand4D.max(axis=0)

#-------------------------------------------------------------------------
#%% Pandas DataFrame

# Os dados vieram de: : https://energiaeambiente.org.br/produto/plataforma-da-qualidade-do-ar

df = pd.read_csv(r"E:\UFSC 2025\Dados\SP\SP201501.csv",
                 encoding='Latin1')

df.describe()
df.info()
df[df.Poluente=='MP10'].Valor.plot()


