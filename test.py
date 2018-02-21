#!/usr/bin/env python
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import time
from matplotlib.backends.backend_pdf import PdfPages
from pylab import *

def trataValores(valores): #transforma os literais em valores inteiro e float, respectivamente, pra uso posterior
    return int(valores[0]), float(valores[1])

def gera_graficos(dataset_name):
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
    j = 0
    size = len(W_data)
    for i in range(0,size):
        a = mdates.datestr2num(str(W_data[i]))
        dias.append(j)
        dias[j] = mdates.num2date(a)
        valores.append(j)
        valores[j] = W_valor[i]
        j = j+1

    hfmt = mdates.DateFormatter('%d/%m/%Y')

    fig, ax = plt.subplots()

    ax.xaxis.set_major_formatter(hfmt)

    plt.plot_date(x=dias, y=valores, fmt="k-", label='original')
    plt.legend(loc='upper right')

    plt.title("Data vs Valor")
    plt.xlabel("Data")
    plt.ylabel("Valor")

    plt.xticks(rotation=60)
    plt.tight_layout()
    plt.grid(True)
#    pdf = PdfPages('test/'+dataset_name+'/test.pdf')
    pdf = PdfPages('test/test.pdf')

    title('test')
    pdf.savefig()
    close()
    pdf.close()

gera_graficos("test")
