#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
from scipy.spatial.distance import euclidean
from fastdtw import fastdtw
import copy

def trataValores(valores): #transforma os literais em valores inteiro e float, respectivamente, pra uso posterior
    return int(valores[0]), float(valores[1])

def main():
    QTD_PREDICT = 10
    k = 8
    dist_list = []
    serie = []
    with open('output.ou') as f: #inicializa os valores de W a partir do arquivo de entrada
        for linha in f:
            linha = linha.strip()
            if linha:
                valores = linha.split(',')
                x,y = trataValores(valores)
                cel = []
                cel.append(x)
                cel.append(y)
                serie.append(cel)

    ini_pos = int(((len(serie)-QTD_PREDICT)/k)*(k-1)) #posição inicial do último pedaço de série antes dos valores quedeverão ser preditos
    comp_serie = []
    another_series = []
    for i in range(ini_pos,len(serie)-11): #joga os valores da última série em comp_serie
        comp_serie.append(serie[i])

    
    for i in range(0, ini_pos, int((len(serie)-QTD_PREDICT)/k)): #percorre a lista de séries e joga os trechos para comparação
        distancia = compare(comp_serie, serie[i:i+int((len(serie)-QTD_PREDICT)/k)])
        dist_list.append(distancia)

    print dist_list
    

    

def compare(list1, list2):
    x = np.array(list1)
    y = np.array(list2)
    distancia, path = fastdtw(x, y, dist=euclidean)
    return distancia

main()
