#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
from scipy.spatial.distance import euclidean
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import accuracy_score
from sklearn.model_selection import GridSearchCV
from sklearn.neighbors import DistanceMetric
from sklearn import preprocessing
from dtw import dtw
import normalization_dtw as ndtw
import time

WIN_SIZE = 50

def trataValores(valores): #transforma os literais em valores inteiro e float, respectivamente, pra uso posterior
    return int(valores[0]), float(valores[1])

def main():
    x = []
    y = []
    y_aux = []
    x_aux = []
    y_saida = []
    # y_plot_unormalized = []
    with open('output.ou') as f: #inicializa os valores de W a partir do arquivo de entrada
        for linha in f:
            linha = linha.strip()
            if linha:
                valores = linha.split(',')
                a,b = trataValores(valores)
                x_aux.append(a)
                y_aux.append(b)

   
    x_aux,y_aux = ndtw.suavizacao(x_aux,y_aux)

    count = 0;
    cel = []
    for i in y_aux[0:int(len(y_aux)*0.8)]: #for que itera até 80% da lista
        count += 1
        y_saida.append(i)
        # y_plot_unormalized.append(i)
        if (count % (WIN_SIZE+1) == 0 and count != 0):
            cel.append(i)
            cel = ndtw.sliding_window_normalizations([],cel,1) #faço as normalizações de janela deslizante
            y.append(cel[-1:]) #o ultimo valor normalizado é meu y
            x.append(cel[:WIN_SIZE])  #os primeiro 4 valores são o meu x
            cel = []
        else:
            cel.append(i)

    
    obj = KNeighborsRegressor(metric=dtw)
    params = {'n_neighbors':range(1,4)} #cria parametros de 1 a 4, o famoso k (nesse caso)
    rsearch = GridSearchCV(obj,params)

    rsearch.fit(x,y) 

    obj = rsearch.best_estimator_ #pega o melhor estimador (no nosso caso, o melhor k ) e executa o knn com este estimador
    obj.fit(x,y)


    for i in range(int(len(y_aux)*0.2)+1): #slicing lists like a BALLLSS
        passar = np.array(y_saida[-WIN_SIZE:]).reshape(1,-1) #transformo a janela em numpy array e dou um reshape pq o knn reclama
        volta = np.copy(passar)
        passar = ndtw.sliding_window_normalizations([],passar,1) #normalizo com a média e desvio padrão
        pred = obj.predict(passar)[0] #pego a predição normalizada
        passar = np.append(passar,pred) #adiciono ela nos valores da qual a predição foi feita
        passar = ndtw.sliding_window_normalizations(volta,passar,0) #tiro a normlização pra jogar na lista de saida
        y_saida.append(passar[-1:]) 

        


    # print rsearch.score(x_test,y_test)
    # print len(x_aux),"\n", len(y_aux),"\n", len(y_saida) #tem que retornar só y_test e res e alterar x_test
    return x_aux,y_aux,y_saida
    
# main() 