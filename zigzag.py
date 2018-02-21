#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division
import collections
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import time
import heapq
import operator
import math

def trataValores(valores): #transforma os literais em valores inteiro e float, respectivamente, pra uso posterior
    return int(valores[0]), float(valores[1])


def zigzag(percent, W_data, W_valor):
    start_time = time.time()
    w_data = []
    w_valor = []
    w_data.append(W_data[0]) #considera o maior valor como sendo o primeiro
    w_valor.append(W_valor[0]) #considera o maior valor como sendo o primeiro
    topo = False
    fundo = False
    indiceFundo = 0
    indiceTopo = 0
    indiceInicio = 0

    for i, val in enumerate(W_valor):

        if(W_valor[i] > W_valor[indiceTopo]):

            indiceTopo = i
            if((not fundo) and ((W_valor[indiceTopo] - W_valor[indiceFundo]) / W_valor[indiceFundo]) * 100 >= percent):
                w_data.append(W_data[indiceFundo])
                w_valor.append(W_valor[indiceFundo])
                topo = False
                fundo = True

            if(fundo):
                indiceFundo = indiceTopo
        else:
            if(W_valor[i] < W_valor[indiceFundo]):

                indiceFundo = i
                if((not topo) and ((W_valor[indiceTopo] - W_valor[indiceFundo]) / W_valor[indiceFundo]) * 100 >= percent):
                    w_data.append(W_data[indiceTopo])
                    w_valor.append(W_valor[indiceTopo])
                    topo = True
                    fundo = False

                if(topo):
                    indiceTopo = indiceFundo

    simpl = []
    # print w_data
    for i, val in enumerate(w_valor):
        cel = []
        cel.append(w_data[i])
        cel.append(val)
        simpl.append(cel)
    cel = []
    cel.append(W_data[len(W_data)-1])
    cel.append(W_valor[len(W_valor)-1])
    simpl.append(cel)
    cel1 = simpl[0] ##############################################################################
    cel2 = simpl[1]
    if(cel1[0] == cel2[0]): ####################### HABEMUS GAMBITO ###############################
        simpl.pop(1)###############################################################################
    temp = time.time() - start_time
    return simpl, W_data, W_valor, temp

def main(pontos,W_data, W_valor):

    #with open('output.ou') as f: #inicializa os valores de W a partir do arquivo de entrada
    #    for linha in f:
    #        linha = linha.strip()
    #        if linha:
    #            valores = linha.split(',')
    #            x,y = trataValores(valores)
    #            W_data.append(x)
    #            W_valor.append(y)

    anterior = 0
    atual = 0
    i = 30
    while(math.fabs(pontos-atual) <= math.fabs(pontos-anterior)):
        anterior = atual
        i = i-0.3
        simpl, wd, ww, temp = zigzag(i, W_data, W_valor)
        atual = len(simpl)
    # print simpl
    print "TEMPO ZIGZAG:",temp
    return simpl, W_data, W_valor, temp
