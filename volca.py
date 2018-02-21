#!/usr/bin/env python
# -*- coding: utf-8 -*-
#!/usr/bin/python
import csv
import sys
import numpy as np
import matplotlib.pyplot as plt
import time
import collections
import copy

class Volca():
    def __init__(self,serie,n):
        self.serie = np.array(serie)
        self.w = int(len(self.serie)/10)
        self.max = [0] * len(serie)
        self.min = [0] * len(serie)
        self.topmax = None
        self.topmin = None
        self.n = n


    def process(self):
        e = 0;
        d = self.w;
        ultimo = len(self.serie) - 1;
        while ((e + self.w) < ultimo ):
            tmax = np.argmax(self.serie[e:d])
            tmin = np.argmin(self.serie[e:d])
            self.max[tmax + e] += 1;
            self.min[tmin + e] += 1;
            e = e +1
            d = d +1
        self.topmax = np.argsort(self.max)
        self.topmin = np.argsort(self.min)

    def simplify(self):
        x = range(len(self.serie))
        topNmax = self.topmax[-int((self.n)/2):]
        topNmin = self.topmin[-int((self.n)/2):]
        x_max = []
        y_max = []
        for i in topNmax:
            x_max.append(i);
            y_max.append(self.serie[i])
        x_min = []
        y_min = []
        for i in topNmin:
            x_min.append(i);
            y_min.append(self.serie[i])

        return x_max, y_max, x_min, y_min

def trataValores(valores): #transforma os literais em valores inteiro e float, respectivamente, pra uso posterior
    return int(valores[0]), float(valores[1])

def main(pontos, W_data, W_valor):
    # W_data = []
    # W_valor = []
    # with open('output.ou') as f: #inicializa os valores de W a partir do arquivo de entrada
    #     for linha in f:
    #         linha = linha.strip()
    #         if linha:
    #             valores = linha.split(',')
    #             x,y = trataValores(valores)
    #             W_data.append(x)
    #             W_valor.append(y)
    start_time = time.time()
    obj = Volca(W_valor, pontos)
    obj.process()
    x_max, y_max, x_min, y_min = obj.simplify()

    simplification = []
    for i, val in enumerate(x_max):
        simplification.append(val)
        simplification.append(x_min[i])

    simplification.append(0)
    simplification.append(len(W_data)-1)
    simplification.sort()
    simpl = []
    for i, val in enumerate(simplification):
        cel = []
        cel.append(W_data[val])
        cel.append(W_valor[val])
        simpl.append(cel)

    temp = time.time() - start_time
    print "TEMPO VOLCA:",temp
    return simpl, W_data, W_valor, temp
