#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pips
import volca as volca
import zigzag
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import time
from matplotlib.backends.backend_pdf import PdfPages
from pylab import *

def trataValores(valores): #transforma os literais em valores inteiro e float, respectivamente, pra uso posterior
    return int(valores[0]), float(valores[1])

def gera_graficos(od_volca, od_pips, od_zigzag, dataset_name, pontos):
    dias_volca = []
    valores_volca = []
    dias_pips = []
    valores_pips = []
    dias_zigzag = []
    valores_zigzag = []
    W_data = []
    W_valor = []

    with open('output.ou') as f: #inicializa os valores de W a partir do arquivo de entrada
        for linha in f:
            linha = linha.strip()
            if linha:
                valores = linha.split(',')
                x,y = trataValores(valores)
                W_data.append(x)
                W_valor.append(y)

    dias = []
    valores = []
    size = len(W_data)
    for i in range(0,size):
        a = mdates.datestr2num(str(W_data[i]))
        dias.append(mdates.num2date(a))
        valores.append(W_valor[i])

    for i, val in enumerate(od_volca):
        a = mdates.datestr2num(str(val[0]))
        dias_volca.append(mdates.num2date(a))
        valores_volca.append(val[1])

    j = 0
    for i, val in enumerate(od_pips):
        a = mdates.datestr2num(str(val[0]))
        dias_pips.append(mdates.num2date(a))
        #print dias[j]
        valores_pips.append(val[1])
        j = j+1

    for i, val in enumerate(od_zigzag):
        a = mdates.datestr2num(str(val[0]))
        dias_zigzag.append(mdates.num2date(a))
        #print dias[j]
        valores_zigzag.append(val[1])


    hfmt = mdates.DateFormatter('%d/%m/%Y')

    fig, ax = plt.subplots()

    ax.xaxis.set_major_formatter(hfmt)

    plt.plot_date(x=dias, y=valores, fmt="k-", label='original')
    plt.plot(dias_volca, valores_volca,'g-',label='volca')
    plt.plot(dias_pips, valores_pips,'b-',label='pips')
    plt.plot(dias_zigzag, valores_zigzag,'r-',label='zigzag')
    plt.legend(loc='upper right')

    plt.title("Data vs Valor")
    plt.xlabel("Data")
    plt.ylabel("Valor")

    plt.xticks(rotation=60)
    plt.tight_layout()
    plt.grid(True)
    pontos = str(pontos)
    pdf = PdfPages('saida/'+dataset_name+'/'+pontos+'pt_vs_original_comp.pdf')
    title(pontos+'pt_vs_original')
    pdf.savefig()
    close()
    pdf.close()
