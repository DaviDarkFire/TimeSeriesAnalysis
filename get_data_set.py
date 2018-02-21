#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pandas_datareader import data
from itertools import islice
import os


def get_data():
    list = []
    #criando uma lista com todos os nomes das bolsa da IBOVESPA
    list.append('ABEV3')
    list.append('BBAS3')
    list.append('BBDC3')
    list.append('BBDC4')
    list.append('BBSE3')
    list.append('BRAP4')
    list.append('BRFS3')
    list.append('BRKM5')
    list.append('BRML3')
    list.append('CCRO3')
    list.append('CIEL3')
    list.append('CMIG4')
    list.append('CPFE3')
    list.append('CPLE6')
    list.append('CSAN3')
    list.append('CSNA3')
    list.append('CYRE3')
    list.append('ECOR3')
    list.append('EGIE3')
    list.append('ELET3')
    list.append('ELET6')
    list.append('EMBR3')
    list.append('ENBR3')
    list.append('EQTL3')
    list.append('ESTC3')
    list.append('FIBR3')
    list.append('GGBR4')
    list.append('GOAU4')
    list.append('HYPE3')
    list.append('ITSA4')
    list.append('ITUB4')
    list.append('JBSS3')
    list.append('KLBN11')
    list.append('KROT3')
    list.append('LAME4')
    list.append('LREN3')
    list.append('MRFG3')
    list.append('MRVE3')
    list.append('MULT3')
    list.append('NATU3')
    list.append('PCAR4')
    list.append('PETR3')
    list.append('PETR4')
    list.append('QUAL3')
    list.append('RADL3')
    list.append('RAIL3')
    list.append('RENT3')
    list.append('SANB11')
    list.append('SBSP3')
    list.append('SMLE3')
    list.append('SUZB5')
    list.append('TIMP3')
    list.append('UGPA3')
    list.append('USIM5')
    list.append('VALE3')
    list.append('VALE5')
    list.append('VIVT4')
    list.append('WEGE3')
    #definindo as datas das quais se deve pegar os valores
    inicio = '2009-02-02'
    fim = '2013-10-25'
    test = '2009'
    #pegando os valores de fato
    for i  in range(0,58,1):
        market = data.DataReader(list[i], 'google', inicio, fim)
        market.to_csv('entrada/'+list[i]+'.csv')
        flag = 0
        with open("entrada/"+list[i]+".csv") as f:                             
            for linha in islice(f,1,2):                
                valores = linha.split(',')
                aux = valores[0].split('-')
                if(test != aux[0]):
                    flag = 1

       # status = os.stat("entrada/"+list[i]+".csv")
       # if(status.st_size <= "4096L"):
       #     flag = 1
                                                          
                
        if(not flag):    
            print 'Mercado: '+list[i] 
        else:
            os.remove("entrada/"+list[i]+".csv")   

get_data()        
