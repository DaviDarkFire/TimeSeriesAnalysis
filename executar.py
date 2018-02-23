#!/usr/bin/env python
# -*- coding: utf-8 -*-
import erro
import gera_graficos as graf
import sys
import os
import clean

def trataValores(valores): #transforma os literais em valores inteiro e float, respectivamente, pra uso posterior
    return int(valores[0]), float(valores[1])

def trataArquivo(file_name): #trata os valores recebidos no arquivo.csv para que assim possamos aplicar os algortimos sobre eles
    print file_name
    s = open("output.ou", "w")
    with open("entrada/"+file_name) as f:
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

def main():
    #pontos = 30
    for file_name in os.listdir("entrada"):
        trataArquivo(file_name)
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

        od_pips, od_volca, od_zigzag = erro.main(file_name, W_data, W_valor)
        #graf.gera_graficos(od_volca, od_pips, od_zigzag, file_name, pontos)
        os.remove("output.ou")
        clean.clear()

#def blau_executa_tudo_esse_cacete():
#    for i in range(5, 105, 5):
#        main(i)

#blau_executa_tudo_esse_cacete()

main()
