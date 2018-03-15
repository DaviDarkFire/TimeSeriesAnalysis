#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
from scipy.spatial.distance import euclidean
from fastdtw import fastdtw
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score


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
                # cel = []
                # cel.append(x)
                # cel.append(y)
                # serie.append(cel)

    x = np.array(x)
    x = x.reshape(x.shape[0],1)
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=4)
    knn = KNeighborsClassifier(n_neighbors=1)
    knn.fit(x_train, y_train)
    pred = knn.predict(x_test.reshape(x_test))
    print accuracy_score(y_test.reshape(y_test))
main()
