#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
from scipy.spatial.distance import euclidean
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.model_selection import GridSearchCV
from sklearn.neighbors import DistanceMetric
from sklearn import preprocessing
from dtw import dtw
from sklearn.neighbors import KNeighborsClassifier
from tslearn.piecewise import SymbolicAggregateApproximation
import normalization_dtw as ndtw
import time

WIN_SIZE = 20 #tamanho da janela deslizante
N_PAA = 100
N_SAX = 100

def trataValores(valores): #transforma os literais em valores inteiro e float, respectivamente, pra uso posterior
    return int(valores[0]), float(valores[1])

def main():
    x = [] #x que será passado para o knn
    y = [] #y que será passado para o knn
    y_aux = [] #valores originais do dataset
    x_aux = [] #datas originais do dataset
    y_saida = [] #possui 80% de seus valores como sendo os valores das bolsas originais e os 20% restante vão ser da prdição
    with open('output.ou') as f: #aqui eu só carrego os valores do meu dataset
        for linha in f:
            linha = linha.strip()
            if linha:
                valores = linha.split(',')
                a,b = trataValores(valores)
                x_aux.append(a)
                y_aux.append(b)

   
    x_aux,y_aux = ndtw.suavizacao(x_aux,y_aux) #função que suaviza os gráficos
    # maior = max(y_aux) #essa e as proximas 2 linhas normalizam os dados pois
    # y_aux = np.array(y_aux)#é necessário que os valores estejam entre
    # y_aux = y_aux/maior#0 e 1 pra que o PAA e consequentemente o SAX funcionem

    y_aux = ndtw.sigmoid(y_aux,1)
    sax = SymbolicAggregateApproximation(n_segments=N_PAA, alphabet_size_avg=N_SAX)
    temp = sax.fit_transform(y_aux)
    classes_sax = []
    for i in temp[0]:
        classes_sax.append(i[0])
     
    count = 0;
    cel = []
    for i in classes_sax[0:int(len(classes_sax)*0.8)]: #for que itera até 80% da lista criando o meu x e y que serão passados pra o knn
        #nesse caso x = [val1, val2, val3,...,valn] e y = val. y tem o tamnho de WIN_SIZE
        #basicamente to criando o dataset de entrada do knn com a janela deslizante
        count += 1
        y_saida.append(i)
        if (count % (WIN_SIZE+1) == 0 and count != 0):
            cel.append(i)
            # cel = ndtw.sliding_window_normalizations([],cel,1) #faço as normalizações com média e desvio padrão
            y.append(cel[-1:]) #o ultimo valor normalizado é meu y
            x.append(cel[:WIN_SIZE])  #os primeiro WIN_SIZE valores são o meu x
            cel = []
        else:
            cel.append(i)

    obj = KNeighborsClassifier(metric=dtw, n_neighbors=1)

    
    # print "\n"
    # print y_saida


    obj.fit(x,y)


    for i in range(int(len(classes_sax)*0.2)+1): #slicing lists like a BALLLSS
        passar = np.array(y_saida[-WIN_SIZE:]).reshape(1,-1) #transformo a janela em numpy array e dou um reshape pq o knn reclama
        pred = obj.predict(passar)[0] #pego a predição normalizada
        passar = np.append(passar,pred) #adiciono ela nos valores da qual a predição foi feita (os valores e a predição estão normalizados)
        y_saida.append(passar[-1:][0]) #coloco o valor obtido na lista de saída 

    saida = []
    saida.append([])

    for i in y_saida:#gambito pq não sei usar reshape
        saida[0].append([i])

    y_saida = sax.inverse_transform(saida)
    y_saida = np.array(y_saida);
    
    saida = [] #se o takashi ver isso ele vai me bater (pray for dave)
    for i in y_saida:#doooooooooooble gambito pq não sei usar reshape
        for j in i:
            for k in j:
                saida.append(k)
    
    y_aux = ndtw.sigmoid(y_aux,0)
    return x_aux,y_aux,saida
    
main() 