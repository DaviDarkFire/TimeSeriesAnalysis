#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
from scipy.spatial.distance import euclidean
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import accuracy_score
from sklearn.model_selection import RandomizedSearchCV
from sklearn.neighbors import DistanceMetric
from sklearn import preprocessing
from dtw import dtw

def trataValores(valores): #transforma os literais em valores inteiro e float, respectivamente, pra uso posterior
    return int(valores[0]), float(valores[1])

def main():
    x = []
    y = []
    with open('output.ou') as f: #inicializa os valores de W a partir do arquivo de entrada
        for linha in f:
            linha = linha.strip()
            if linha:
                valores = linha.split(',')
                a,b = trataValores(valores)
                y.append(b)
    
    y_aux = []
    x_aux = []
    count = 0;
    cel = []
    for i in y:
        count += 1
        if (count % 5 == 0 and count != 0):
            y_aux.append(i)
            x_aux.append(cel)
            cel = []
        else:
            cel.append(i)

        
    print np.array(x_aux)
    # print y_aux
    # y = np.array(y)
    # x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=4)
    # knn = KNeighborsRegressor(n_neighbors=1, metric=dtw)
    # knn.fit(x_train, y_train)
    # pred = knn.predict(x_test)
    # return x_test, y_test, pred
main()