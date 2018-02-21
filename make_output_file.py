#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os

def trataValores(valores): #transforma os literais em valores inteiro e float, respectivamente, pra uso posterior
    return int(valores[0]), float(valores[1])

def trataArquivo(): #trata os valores recebidos no arquivo.csv para que assim possamos aplicar os algortimos sobre eles
    file_name = sys.argv[1]
    s = open("output.ou", "w")
    with open(file_name) as f:
        flag = 0
        for linha in f:
            if (flag):
                linha = linha.strip()
                if linha:
                    valores = linha.split(',')
                    data = valores[0]
                    close = valores[4]
                    data_aux = data.split("-")
                    data = data_aux[0]+data_aux[1]+data_aux[2]

                    s.write(data) #gambito
                    s.write(',')
                    s.write(close)# dooooooooouble gambito
                    s.write('\n')
            else:
                flag = 1
    f.close()
    s.close()


trataArquivo()
