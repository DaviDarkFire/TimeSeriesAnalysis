#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
from scipy.spatial.distance import euclidean
from fastdtw import fastdtw
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
from sklearn import preprocessing


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
                x.append(a)
                y.append(b)

    # x = np.zeros((len(x_aux), 3))
    # for i, val in enumerate(x_aux):
    #     x[i][2] = x_aux[i]%100
    #     # print x_aux[i]%100
    #     x_aux[i] /= 100 
    #     x[i][1] = x_aux[i]%100
    #     # print x_aux[i]%100
    #     x_aux[i] /= 100
    #     x[i][0] = x_aux[i]
    #     # print x_aux[i]
    #     # print "\n"
    # np.set_printoptions(threshold='nan')
    
    x = np.array(x)
    x = x.reshape(x.shape[0],1)
    y = np.array(y)
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=4)
    knn = KNeighborsRegressor(n_neighbors=1)
    knn.fit(x_train, y_train)
    pred = knn.predict(x_test)
    return knn.score(x_test,y_test)