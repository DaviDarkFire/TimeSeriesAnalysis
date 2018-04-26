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

def suavizacao():
    x,y = get_data()
    x_exit = []
    y_exit = []
    for i in range(0,len(y)-3,3):
        y_exit.append((y[i]+y[i+1]+y[i+2])/3)
        x_exit.append(x[i+1])

    return x,y,x_exit,y_exit


def sliding_window_normalizations():
    print "Code"

suavizacao()