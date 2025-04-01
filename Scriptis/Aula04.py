# -*- coding: utf-8 -*-
"""
Created on Tue Apr  1 13:52:42 2025

Este scripti utilizei durante a aula 04 do dia 01/04/2025


@author: Julia
"""

#%%% Importando os pacotes que utilizarei 

import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt 
import os 

#%% Revisão numpy 

# Criando um vetor com arranjo de dados 
x = np.arange(-10,20,0.15)

# Brincando com indexação 
print('Esta é a quarta posição do meu vetor x:' + str(x[3]))

print ('Estes são os 3 primeiros valores' + str(x[0:3]))

# Substituir um valor dentro do vetor 
x[9]= 9999999999 #Exemplo de medição errada 
x [11] = -9999999999 #Exemplo de medição errada 

# Extraindo a média 
meanX = np.mean(x)
print (meanX)

# Operação booleana
# and = &
# or = | 
# Encontrando valores errados 
vecBoo1 = (x>20) | (x<-10) 

# EXtraindo valores errados usando lógica boleana
valErrado = x[vecBoo1]

# Substituindo os valores errados por zero 
x2 = x.copy() # Criando uma cópia independente 
x2[vecBoo1] = 0
print("Esta é a média de x substituindo os valores errados por 0:" +
      str(np.mean(x2)))

# Substituindo por Nan - Not  a number 
x3 = x.copy() # Criando uma cópia independente 
x3[vecBoo1] = np.nan
print("Esta é a média de x substituindo os valores errados por nan:" +
      str(np.mean(x3)))

print("Esta é a média usando np.nanmean de x substituindo os valores errados por nan:" +
      str(np.nanmean(x3)))

# Substituindo pela média 
x4 = x.copy()
x4[vecBoo1] = np.nanmean(x3)
print("Esta é a média de x substituindo os valores errados por nan:" +
      str(np.mean(x4)))

#%% Usando matplotlib para inspecionar os vetotes

fig, ax = plt.subplots(4)
ax[0].plot(x)
ax[1].plot(x2)
ax[2].plot(x3)
ax[3].plot(x4)


#%% Loop em Python

# Loop utilizando Range 
for ii in range(0,10):
    val = 2**ii 
    print (val)
    
# Loop utilizando Range e acumulando em um vetor 
vetor = []
for ii in range(0,10):
    val = 2**ii 
    vetor.append(val)

# Loop utilizando Range e acumulando o valor de val
vetorAcumulado = []
val = 0 
for ii in range(0,10):
    val = val+2**ii 
    vetorAcumulado.append(val)


# Loop utilizando uma lista 

alunas = ['Mariana', 'Bianca','Ana Júlia', 'Mariah']

for aluna in alunas :
    print ('A nota da prova '+aluna+' é:' + str(np.random.rand(1)*10))

#%% Trabalhando com o Pandas

# Criando um DataFrame manualmenete 

df = pd.DataFrame(columns=['date', 'NH3'], 
                  data=[
                      ['2025/04/01', 0.35],
                      ['2025/04/02', 1.01]
                      ])

# Criando mais coisas dentro do df
df['NO3'] = np.nan 
df['O2'] = [2,10]
df['S04'] = np.nan
df['S04'][0] = 10

# Trabalhando com dados reais 
uf = 'MG'

# Definindo caminho para a pasta de dados 
dataDir = r"E:\UFSC 2025\ENS5132\data\MQAR"+ '/' + uf 

# Lista de arquivos dentro da pasta
dataList = os.listdir(dataDir)

#Movendo para a pasta de dados/uf
os.chdir(dataDir)

for fileInList in dataList:
    print(fileInList)
    dfConc= pd.read_csv(fileInList, encoding='latin1')
    allFiles.append(dfConc)

# Concatenando meus DataFrames
allFiles = pd.concat(allFiles)

#Extraindo nomes das estações sem redundância 
stations = pd.unique(allFiles['Estacao'])

#Usando lógica 
stationDf = allFiles(allFiles['Estacao'== station[0]])

#Criando coluna datatime
datetieDf = pd.to_datetime(stationDf.Data, format = '%Y-%m-%d')

#criando coluna datetime dentro de stationDf
stationDf['datetime'] = datetimeDf

# Trandformando a coluna de datetime em index
stationDf = stationDf.set_index(stationDf['datatime'])

#Extrair o ano 
stationDf['year'] = stationDf.index.year
stationDf['month'] = stationDf.index.month
stationDf['day'] = stationDf.index.day

#extraindo a hora 
horas = stationDf.Hora.str.split(':')

for hora in horas:
    print(horas[0])
    horaDf.append(hora[0])
    
stationDf['hour'] = horaDf

# Corrigindo a coluna datetime

stationDf['datetime'] = pd.to_datetime(stationDf.astype(str).year +
                                       stationDf.astype(str).month +
                                       stationDf.astype(str).day +
                                       stationDf.astype(str).hour, 
                                       format='%Y%m%d5H')






