"""
Created on Tue Apr  8 15:32:16 2025

Lembre-se de criar as pastas corretamente


"""

# Importação de pacotes
from airQualityAnalysis import airQualityAnalysis
from airQualityFigures import airQualityHist, airQualityTimeSeries
import os
from univariateStatistics import univariateStatistics
import sys

# Usando os.getcwd() para garantir que o diretório de trabalho seja correto em qualquer ambiente
repoPath = os.getcwd()  # Em Jupyter, usar getcwd em vez de __file__
print(f'Repositório encontrado em: {repoPath}')

# Definindo pasta de dados
dataPath = os.path.join(repoPath, 'inputs')  # Usar os.path.join para construir caminhos de maneira segura
print(f'Caminho dos dados: {dataPath}')

# Cria a pasta se ela não existir... precisam colocar os dados dentro dela.
os.makedirs(dataPath, exist_ok=True)

# Lista pastas dentro de dataPath
ufs = os.listdir(dataPath)

# Loop para todos os estados
for uf in ufs:
    
    # Chamando a função para analisar a qualidade do ar
    aqData, stations, aqTable = airQualityAnalysis(uf, repoPath)
    
    # Mudando para o diretório correto onde os scripts estão localizados
    scriptsPath = os.path.join(repoPath, 'scripts')  # Garantir que o caminho está correto
    os.chdir(scriptsPath)
    
    # Gerar figuras, descomente se necessário
    # airQualityHist(aqData, stations, uf, repoPath)
    # airQualityTimeSeries(aqData, stations, uf, repoPath)
    
    # Gerar estatísticas univariadas
    univariateStatistics(aqTable, stations, uf, repoPath)



