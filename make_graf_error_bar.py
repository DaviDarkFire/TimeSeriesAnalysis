#!/usr/bin/env python
# -*- coding: utf-8 -*-
import csv
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import math
from matplotlib.backends.backend_pdf import PdfPages
from pylab import *

QTD_DATASETS = 43

def gets_data(algorithm_name):
    media = []
    pontos = []
    for i in range(0,20):
        media.append(0.0)

    with open('new_saida/'+algorithm_name+'.csv', 'rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        j = 0
        for row in spamreader:
            if(j != 0 and j != QTD_DATASETS+1):

                for i, val in enumerate(row):
                    if (i > 0):
                        media[i-1] = float(val)+media[i-1]
            # else:
            #     print row
            #     print "\n"
            j = j+1

    for i, val in enumerate(media):
        media[i] = media[i]/QTD_DATASETS

    ponto = 5
    for i in range(0,20):
        pontos.append(ponto)
        ponto = ponto+5

    return media, pontos

def calc_raio(media):
    variancia = 0
    standard_error = 0
    x_barra = 0

    for i, val in enumerate(media):############################################
        x_barra = x_barra+val       #cálculo do x barra
    x_barra = x_barra/len(media)####################################


    for i, val in enumerate(media):############################################
        aux = val-x_barra
        aux = aux*aux #cálculo da variância
        variancia = aux+variancia
    variancia = variancia/len(media)
    desvio_padrao = math.sqrt(variancia)############################################

    standard_error = desvio_padrao/math.sqrt(QTD_DATASETS)


    return standard_error

def gera_grafico_error_bar(pontos, media_pips, media_volca, media_zigzag, name, raio_pips, raio_volca, raio_zigzag):
    fig, ax = plt.subplots()
    ls = 'line'
    # plt.plot(pontos, media_pips,'b-',label=name+' Pips')
    # plt.plot(pontos, media_volca,'g-',label=name+' Volca')
    # plt.plot(pontos, media_zigzag,'r-',label=name+' Zigzag')


    plt.errorbar(pontos, media_pips, xerr=0, yerr=raio_pips, color='blue', label = "Pips")
    plt.errorbar(pontos, media_volca, xerr=0, yerr=raio_volca, color='green', label = "Volca")
    plt.errorbar(pontos, media_zigzag, xerr=0, yerr=raio_zigzag, color='red', label = "Zigzag")

    plt.legend(loc='upper right')
    plt.title("Pontos vs "+name)
    plt.xlabel("Pontos")
    plt.ylabel(name)
    plt.xticks(rotation=60)
    plt.tight_layout()
    plt.grid(True)
    pdf = PdfPages('new_saida/Pontos vs '+name+'.pdf')
    title('Plot')
    pdf.savefig()
    close()
    pdf.close()

def main():
    media_pips, pontos = gets_data("saida_pips")
    media_volca, pontos = gets_data("saida_volca")
    media_zigzag, pontos = gets_data("saida_zigzag")
    raio_pips = calc_raio(media_pips)
    raio_volca = calc_raio(media_volca)
    raio_zigzag = calc_raio(media_zigzag)
    gera_grafico_error_bar(pontos, media_pips, media_volca, media_zigzag, "Erro", raio_pips, raio_volca, raio_zigzag)

main()
