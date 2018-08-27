#!/usr/bin/env python
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.backends.backend_pdf import PdfPages
import numpy as np

e = 2.718281828459045235360287
a = 0.0000001

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

def sigmoid(y, flag):
    if (flag):
        for i, j in enumerate(y):
            print "/////////////////"
            print j
            y[i] = 1/(1+e**(-1*j))

            print y[i]
            print "****************"
            print "\n"
    else:
        for i, j in enumerate(y):
            if (j != 0):
                y[i] = -1*np.log((1/j)-1)
            else:
                y[i] = -1*np.log((1/a)-1)
    return y

def suavizacao(x,y):
    # x,y = get_data()
    x_exit = []
    y_exit = []
    for i in range(0,len(y)-3,3): #faço a média dos 3 valores em sequencia para normalizar
        y_exit.append((y[i]+y[i+1]+y[i+2])/3)
        x_exit.append(x[i+1])

    return x_exit,y_exit


def sliding_window_normalizations(volta,lista,flag):#se flag == 1 fazemos a normalização se flag == 0 voltamos a normalização
    lista = np.array(lista)
    desp = np.std(lista) #cálculo desvio padrão
    media = np.mean(lista) #cálculo média
    if flag:
        print "normalização \n"
        print "original: ", lista
        if desp <= 0.01: #trashold para evitar o desvio padrão de ficar muito pequeno e estourar a memória
            desp = 0.01
        lista = (lista - media)/desp #cálculo da normalização em todos os valores de lista
        # print "norm"
        # print lista

        
        

        print "desvio padrão: ", desp
        print "média: ", media
        print lista
        print "///////////////////////////////////"
    else:
        #seção do código que volta da normalização, ou seja volta os valores originais
        volta = np.array(volta) 
        desp = np.std(volta) #cáculo do desvio padrão
        media = np.mean(volta) #cálculo da média
        if desp <= 0.01: #o mesmo trashold
            desp = 0.01

        print "volta da normalização \n"
        print "desvio padrão: ", desp
        print "média: ", media

        lista = lista*desp + media #aplicando a volta da normalização nos valores da lista normalizada
        # print "volta"
        # print volta
        print lista
        print "///////////////////////////////////"

    return lista
