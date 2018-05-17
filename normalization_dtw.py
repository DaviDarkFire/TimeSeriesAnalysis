#!/usr/bin/env python
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.backends.backend_pdf import PdfPages
import numpy as np

def trataValores(valores): #transforma os literais em valores inteiro e float, respectivamente, pra uso posterior
    return int(valores[0]), float(valores[1]) 

def get_data():
    x = []
    y = []
    with open('output.ou') as f:
        for linha in f:
            linha = linha.strip()
            if linha:
                valores = linha.split(',')
                a,b = trataValores(valores)
                x.append(a)
                y.append(b)
    return x,y

def suavizacao(x,y):
    # x,y = get_data()
    x_exit = []
    y_exit = []
    for i in range(0,len(y)-3,3):
        y_exit.append((y[i]+y[i+1]+y[i+2])/3)
        x_exit.append(x[i+1])

    return x_exit,y_exit


def sliding_window_normalizations(volta,lista,flag):#se flag == 1 fazemos a normalização se flag == 0 voltamos a normalização
    lista = np.array(lista)
    desp = np.std(lista)
    media = np.mean(lista)
    if flag:
        print "normalização \n"
        print "original: ", lista
        if desp <= 0.01:
            desp = 0.01
        lista = (lista - media)/desp
        # print "norm"
        # print lista

        
        

        print "desvio padrão: ", desp
        print "média: ", media
        print lista
        print "///////////////////////////////////"
    else:
        volta = np.array(volta)
        desp = np.std(volta)
        media = np.mean(volta)
        if desp <= 0.01:
            desp = 0.01

        print "volta da normalização \n"
        print "desvio padrão: ", desp
        print "média: ", media

        lista = lista*desp + media
        # print "volta"
        # print volta
        print lista
        print "///////////////////////////////////"

    return lista
