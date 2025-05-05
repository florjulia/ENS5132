import matplotlib.pyplot as plt
import os
import numpy as np
from scipy import stats
import statsmodels.api as sm
import pandas as pd

# Função para criar o histograma
def airQualityHist(aqData, stations, uf, repoPath):
    # Cria a pasta de saída, caso não exista
    os.makedirs(repoPath+'/figuras/'+uf, exist_ok=True)
    
    # Loop para cada estação
    for st in stations:
        fig, ax = plt.subplots()
        # Cria o histograma por poluente
        aqData[aqData.Estacao == st].hist('Valor', by='Poluente', ax=ax)
        # Cria o diretório de destino, caso não exista
        save_path = repoPath + '/figuras/' + uf + '/hist_' + st
        os.makedirs(save_path, exist_ok=True)
        # Salva o gráfico
        fig.savefig(repoPath+'/figuras/'+uf+'/hist_'+st+'.png')

# Função para criar os gráficos de séries temporais
def airQualityTimeSeries(aqData, stations, uf, repoPath):
    # Cria a pasta de saída, caso não exista
    os.makedirs(repoPath+'/figuras/'+uf, exist_ok=True)
    
    # Loop para cada estação
    for st in stations:
        # Extraindo os poluentes para a estação atual
        pollutants = np.unique(aqData[aqData.Estacao == st].Poluente)
        
        # Criando figura com número de poluentes
        fig, ax = plt.subplots(pollutants.size if pollutants.size > 1 else 1)
        
        # Loop para cada poluente
        for ii, pol in enumerate(pollutants):
            if pollutants.size > 1:
                ax[ii].plot(aqData[(aqData.Estacao == st) & (aqData.Poluente == pol)].Valor)
            else:
                ax.plot(aqData[(aqData.Estacao == st) & (aqData.Poluente == pol)].Valor)
        
        # Salva a figura após o loop
        fig.savefig(repoPath+'/figuras/'+uf+'/plot_'+st+'.png')

# Função para verificar a normalidade dos dados
def normalityCheck(aqTableAlvo, repoPath, uf, stationAlvo, pol):
    # Figura para verificar a distribuição dos dados 
    fig, ax = plt.subplots(3)
    ax[0].hist(np.log(aqTableAlvo[pol].dropna()), facecolor='red')
    ax[0].set_title('Log')
    ax[0].set_ylabel('Frequência')
    ax[1].hist(stats.boxcox(aqTableAlvo[pol].dropna()), facecolor='green')
    ax[1].set_title('Boxcox')
    ax[1].set_ylabel('Frequência')
    ax[2].hist(aqTableAlvo[pol].dropna())
    ax[2].set_title('Dado original')
    ax[2].set_ylabel('Frequência')
    fig.tight_layout() 
    # Salva o gráfico da normalidade
    fig.savefig(repoPath+'/figuras/'+uf+'/histogramDataNormalization_'+pol+'_'+stationAlvo+'.png')
    return fig

# Função para criar os gráficos de tendência
def trendFigures(data, result):
    fig, ax = plt.subplots(2)
    sm.graphics.tsa.plot_acf(data, lags=5, ax=ax[0])
    ax[0].set_title('Autocorrelação ACF')
    trend_line = np.arange(len(data)) * result.slope + result.intercept
    data.plot(ax=ax[1])
    ax[1].plot(data.index, trend_line)
    ax[1].legend(['data', 'trend line'])
    ax[1].set_title('Tendência')
    return fig

# Função para previsão de séries temporais
def timeSeriesForecast(complete_data, repoPath, uf, pol, stationAlvo):
    from pmdarima.arima import auto_arima

    # Criando o modelo auto-arima
    stepwise_model = auto_arima(complete_data, start_p=1, start_q=1, max_p=3, max_q=3, m=12,
                       seasonal=True, error_action='ignore')

    print(stepwise_model.aic())
    
    # Segregando grupo de treinamento e teste
    train = pd.DataFrame({'train': complete_data.iloc[0:int(complete_data.shape[0]*0.7)]})
    test = pd.DataFrame({'test': complete_data.iloc[int(complete_data.shape[0]*0.7):]})
    
    # Calibrando o modelo
    stepwise_model.fit(train)
    
    # Fazendo a previsão futura
    future_forecast = pd.DataFrame({'future_forecast': stepwise_model.predict(n_periods=test.shape[0])})
    
    # Criando o gráfico da previsão
    fig, axes = plt.subplots()
    pd.concat([complete_data, future_forecast], axis=1).plot(ax=axes) 
    
    # Salvando o gráfico da previsão
    fig.savefig(repoPath+'/figuras/'+uf+'/timeSeriesForecast'+pol+'_'+stationAlvo+'.png')
    return fig
