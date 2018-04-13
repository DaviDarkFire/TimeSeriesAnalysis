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
    with open('output.ou') as f: #inicializa os valores de W a partir do arquivo de entrada
        for linha in f:
            linha = linha.strip()
            if linha:
                valores = linha.split(',')
                a,b = trataValores(valores)
                y_aux.append(b)
    
    count = 0;
    cel = []
    for i in y_aux:
        count += 1
        if (count % 5 == 0 and count != 0):
            y.append(i)
            x.append(cel)
            cel = []
        else:
            cel.append(i)

        

    x_train, x_test, y_train, y_test=train_test_split(x,y,test_size=0.20)

    # print x_train
    # print x_test

    start = time.time()
    
    obj = KNeighborsRegressor(metric=dtw)
    params = {'n_neighbors':range(1,4)} #cria parametros de 1 a 50, o famoso k (nesse caso)
    rsearch = GridSearchCV(obj,params)

    # print np.array(x_train)
    # print np.array(y_train)

    rsearch.fit(np.array(x_train),np.array(y_train)) 
    # print y_train
    print rsearch.best_score_
    print rsearch.best_params_

    obj = rsearch.best_estimator_ #pega o melhor estimador (no nosso caso, o melhor k ) e executa o knn com este estimador
    obj.fit(x_train,y_train)
    res = obj.predict(x_test)
    print rsearch.score(x_test,y_test)
    return x_test, y_test, res #tem que retornar só y_test e res e alterar x_test
    # print time.time() - start
    # print y_aux
    # y = np.array(y)
    # x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=4)
    # knn = KNeighborsRegressor(n_neighbors=1, metric=dtw)
    # knn.fit(x_train, y_train)
    # pred = knn.predict(x_test)
    # return x_test, y_test, pred
main()