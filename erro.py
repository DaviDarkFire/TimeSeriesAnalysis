#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import zigzag
import volca
import pips
import os
from matplotlib.backends.backend_pdf import PdfPages
from pylab import *
import generate_simplifications
import gera_graficos as graficos

def calc_reta(x1,y1,x2,y2): #função que calcula reta que liga os dois pontos mais próximos da simplificação
    # print "x1: "+str(y1), "x2: "+str(y2)
    m = (float(y2-y1))/(float(x2-x1))
    a = -m*float(x1)+float(y1)
    return m, a

def calc_erro(od, W_data, W_valor): #sabendo agora a equação da reta podemos gerar pontos sobre e assim calcular o erro através da diferença
    od_data = []
    od_valor = []
    erro = 0
    for i, val in enumerate(od): #passa o valor do dicionário ṕara listas para que a manipulação dos dados fique mais fácil
        od_data.append(val[0])
        od_valor.append(val[1])

    for i in range(0,len(od_data)): #percorre a lista das datas após a simplificação
    	if(i < len(od_data)-1): #a verificação serve para não termos erros de indice quando fizermos conta mais a frente com i+1

            j = W_data.index(od_data[i])
            k = W_data.index(od_data[i+1])
            m, a = calc_reta(od_data[i], od_valor[i], od_data[i+1], od_valor[i+1]) #calcula os coeficientes angulares e lineares da reta m e a respectivamente

            for l, val in enumerate(W_data[j:k+1]): #calcula o ponto sobre a reta e subtrai do ponto original
            	y = val*m+a
            	erro = abs(W_valor[l+j]-y)+erro
    return erro


def erro_vs_pontos(w_mod, W_data, W_valor):
    temp_pips = 0
    temp_volca = 0
    temp_zigzag = 0

    od_pips, W_data_aux, W_valor, temp_pips = pips.main(w_mod, W_data, W_valor)
    erro_pips = calc_erro(od_pips, W_data, W_valor)

    od_volca, W_data_aux, W_valor, temp_volca = volca.main(w_mod, W_data, W_valor)
    erro_volca = calc_erro(od_volca, W_data, W_valor)

    od_zigzag, W_data_aux, W_valor, temp_zigzag = zigzag.main(w_mod, W_data, W_valor)
    erro_zigzag = calc_erro(od_zigzag, W_data, W_valor)

    return temp_pips, temp_volca, temp_zigzag, erro_pips, erro_volca, erro_zigzag, od_pips, od_volca, od_zigzag


def graf(x, y, z, w, name, dataset_name):
    fig, ax = plt.subplots()
    plt.plot(x, y,'b-',label=name+' Pips')
    plt.plot(x, z,'g-',label=name+' Volca')
    plt.plot(x, w,'r-',label=name+' Zigzag')

    plt.legend(loc='upper right')
    plt.title("Pontos vs "+name)
    plt.xlabel("Pontos")
    plt.ylabel(name)
    plt.xticks(rotation=60)
    plt.tight_layout()
    plt.grid(True)
    pdf = PdfPages('saida/'+dataset_name+'/Pontos vs '+name+'.pdf')
    title('Plot')
    pdf.savefig()
    close()
    pdf.close()

def main(dataset_name, W_data, W_valor):
    od_pips = []
    od_volca = []
    od_zigzag = []
    if not os.path.exists("saida/"+dataset_name):
        os.makedirs("saida/"+dataset_name)
    saida = open("saida/"+dataset_name+"/erro_tempo_vs_pontos.csv", "w")
    saida.write('"Quantidade de Pontos"')
    saida.write(',')
    saida.write('Tempo Pips')
    saida.write(',')
    saida.write('Erro Pips')
    saida.write(',')
    saida.write('Tempo Volca')
    saida.write(',')
    saida.write('Erro Volca')
    saida.write(',')
    saida.write('Tempo Zigzag')
    saida.write(',')
    saida.write('Erro Zigzag')
    saida.write('\n')

    total = 100
    passo = 5
    total1 = total+5

    tp = [] #essas são as listas q1ue serão passadas para gerar os gráficos de erro e de tempo
    tv = []
    tz = []
    ep = []
    ev = []
    ez = []
    p = []

    for i in range(5, total1, passo):
        temp_pips, temp_volca, temp_zigzag, erro_pips, erro_volca, erro_zigzag, od_pips, od_volca, od_zigzag = erro_vs_pontos(i, W_data, W_valor)
        tp.append(temp_pips)
        tv.append(temp_volca)
        tz.append(temp_zigzag)
        ep.append(erro_pips)
        ev.append(erro_volca)
        ez.append(erro_zigzag)
        p.append(i)

        saida.write(str(i))
        saida.write(',')
        saida.write(str(temp_pips))
        saida.write(',')
        saida.write(str(erro_pips))
        saida.write(',')
        saida.write(str(temp_volca))
        saida.write(',')
        saida.write(str(erro_volca))
        saida.write(',')
        saida.write(str(temp_zigzag))
        saida.write(',')
        saida.write(str(erro_zigzag))
        saida.write('\n')
        generate_simplifications.main(i, dataset_name,od_pips, od_volca, od_zigzag)
        graficos.gera_graficos(od_volca, od_pips, od_zigzag, dataset_name, i)
    saida.close()
    graf(p, ep, ev, ez, "Erro", dataset_name)
    graf(p, tp, tv, tz, "Tempo", dataset_name)
    #for i in range(5, 105, 5):
        #temp_pips, temp_volca, temp_zigzag, erro_pips, erro_volca, erro_zigzag, od_pips, od_volca, od_zigzag = erro_vs_pontos(i, W_data, W_valor)
    return od_pips, od_volca, od_zigzag
