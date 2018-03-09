#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
from scipy.spatial.distance import euclidean
from fastdtw import fastdtw
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression



def trataValores(valores): #transforma os literais em valores inteiro e float, respectivamente, pra uso posterior
    return int(valores[0]), float(valores[1])

def main():
    serie = []
    with open('output.ou') as f: #inicializa os valores de W a partir do arquivo de entrada
        for linha in f:
            linha = linha.strip()
            if linha:
                valores = linha.split(',')
                x,y = trataValores(valores)
                # cel = []
                # cel.append(x)
                # cel.append(y)
                serie.append(y)

    serie = np.matrix(serie)
    fim_x = int(len(serie)*0.5)

    x = serie[0:fim_x]
    y = serie[fim_x:len(serie)-1] 
    X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=4)
    logreg = LogisticRegression()
    logreg.fit(X_train, y_train)
    y_pred = logreg.predict(X_test)
    # print metrics.accuracy_score(y_test, y_pred)
main()