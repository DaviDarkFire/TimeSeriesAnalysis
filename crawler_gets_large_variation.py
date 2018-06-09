#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import make_output_file as mkof
from shutil import copyfile

PERCENT = 0.5

def trataValores(valores): #transforma os literais em valores inteiro e float, respectivamente, pra uso posterior
    return int(valores[0]), float(valores[1])

def crawl():
    rootdir = 'entrada/'
    for subdir, dirs, files in os.walk(rootdir):
        for file in files:
            mkof.trataArquivo(rootdir+file)
            if trashold(PERCENT):
                copyfile(rootdir+file,'datasets_grandes_variacoes/'+file)

def trashold(percent):
    data = []
    valor = []
    with open('output.ou') as f: #inicializa os valores de W a partir do arquivo de entrada
       for linha in f:
           linha = linha.strip()
           if linha:
               valores = linha.split(',')
               x,y = trataValores(valores)
               data.append(x)
               valor.append(y)

    anterior = max(valor)
    for i in valor:
        if(i >= anterior*percent+anterior or i <= anterior-anterior*percent):
            return True
        anterior = i

    return False

crawl()