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
import time

def trataValores(valores): #transforma os literais em valores inteiro e float, respectivamente, pra uso posterior
    return int(valores[0]), float(valores[1])

def main():
    x = []
    y = []
    y_aux = []
    x_aux = []
    y_saida = []
    with open('output.ou') as f: #inicializa os valores de W a partir do arquivo de entrada
        for linha in f:
            linha = linha.strip()
            if linha:
                valores = linha.split(',')
                a,b = trataValores(valores)
                x_aux.append(a)
                y_aux.append(b)

    
    

    count = 0;
    cel = []
    for i in y_aux[0:int(len(y_aux)*0.8)]: #for que itera até 80% da lista
        count += 1
        y_saida.append(i)
        if (count % 5 == 0 and count != 0):
            y.append(i)
            x.append(cel)
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
        passar = np.array(y_saida[-4:]).reshape(1,-1) #transformo a janela em numpy array e dou um reshape pq o knn reclama
        y_saida.append(obj.predict(passar)[0]) #janela deslizante fazendo predições, essa posição [0] é pq o retorno do predict é uma np.array com uma posição que tem o valor que eu quero

    # print rsearch.score(x_test,y_test)
    # print len(x_aux),"\n", len(y_aux),"\n", len(y_saida) #tem que retornar só y_test e res e alterar x_test
    return x_aux,y_aux,y_saida
    
# main()