"""
Created on Sun Apr 27 21:32:05 2025

@author: Julia

"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# pip install scikit-learn
from sklearn.linear_model import LinearRegression
from sklearn import svm

def multivariateStatistics(aqTable, station_index=10):
    """
    Função para realizar estatísticas multivariadas nos dados de qualidade do ar.
    
    Parâmetros:
    aqTable (DataFrame): Tabela contendo os dados de qualidade do ar.
    station_index (int): Índice da estação que será analisada. O padrão é 10.
    
    Retorno:
    None (salva as figuras geradas)
    """
    
    # Selecionando os dados da estação alvo
    aqTableAlvo = aqTable.reset_index()[aqTable.reset_index()['Estacao'] == aqTable['Estacao'].unique()[station_index]].iloc[:, 3:]

    # Boxplot dos dados comparando todos os poluentes
    fig, ax = plt.subplots(2)
    sns.boxplot(data=aqTableAlvo, ax=ax[0])
    sns.violinplot(data=aqTableAlvo, ax=ax[1])
    ax[0].set_title('Boxplot')
    ax[1].set_title('Violin Plot')
    plt.tight_layout()
    fig.savefig('boxplot_violin_plot.png')
    
    # Pairplot
    fig, ax = plt.subplots()
    sns.pairplot(aqTableAlvo)
    plt.suptitle("Pairplot", y=1.02)
    fig.savefig('pairplot.png')
    
    # Regplot
    fig, ax = plt.subplots()
    sns.regplot(x='NO', y='NO2', data=aqTableAlvo)
    ax.set_title('Regplot: NO vs NO2')
    fig.savefig('regplot_no_vs_no2.png')
    
    # PairGrid
    fig, ax = plt.subplots()
    g = sns.PairGrid(aqTableAlvo)
    g = g.map_upper(sns.scatterplot)
    g = g.map_lower(sns.kdeplot)
    g = g.map_diag(sns.kdeplot, lw=2)
    g.fig.suptitle("PairGrid")
    plt.tight_layout()
    fig.savefig('pairgrid.png')
    
    # Matriz de correlação
    fig, ax = plt.subplots()
    corr = aqTableAlvo.corr()
    corr.style.background_gradient(cmap='coolwarm', axis=None)
    sns.heatmap(corr, cmap='coolwarm')
    ax.set_title('Matriz de Correlação')
    fig.savefig('correlation_heatmap.png')

    # Regressão linear multivariada
    # Eliminando colunas com NaN e linhas com NaN
    regData = np.array(aqTableAlvo[['MP10', 'NO', 'NO2', 'O3']].copy().dropna(axis=0))

    # Aplicando a regressão - fit = otimização dos parâmetros do modelo
    reg = LinearRegression().fit(regData[:, 1:], regData[:, 0])

    # Erro quadrado do modelo
    r2_score = reg.score(regData[:, 1:], regData[:, 0])
    print(f"R² (Erro quadrado do modelo): {r2_score:.4f}")

    # Coeficientes da equação
    print("Coeficientes da regressão:", reg.coef_)

    # Previsão
    prediction = reg.predict(np.array([[10, 100, 100]]))
    print(f"Previsão para dados [10, 100, 100]: {prediction}")

    # Usando aprendizagem de máquina (SVM)
    clf = svm.SVC()
    clf.fit(regData[:, 1:], regData[:, 0])

    # Score do SVM
    clf_score = clf.score(regData[:, 1:], regData[:, 0])
    print(f"Score do SVM: {clf_score:.4f}")

    # Previsão com SVM
    clf_prediction = clf.predict(np.array([[10, 100, 100]]))
    print(f"Previsão com SVM para dados [10, 100, 100]: {clf_prediction}")

    return
