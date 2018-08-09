#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tslearn.piecewise import PiecewiseAggregateApproximation
from tslearn.piecewise import SymbolicAggregateApproximation

from tslearn.generators import random_walks
from tslearn.preprocessing import TimeSeriesScalerMeanVariance
import numpy as np

class Transform:
    n_paa = 0
    n_sax = 0
    dataset = [] #dataset norma
    norm_dataset = [] #dataset normalizado
    trans_dataset = [] #dataset após transformação paa_sax
    invTrans_dataset = [] #dataset após transformação inversa

    def __init__(self, n_paa, n_sax):
        self.n_paa = n_paa
        self.n_sax = n_sax

    def transform(self, data=None):
        sax = SymbolicAggregateApproximation(n_segments=self.n_paa, alphabet_size_avg=self.n_sax)    
        self.trans_dataset = sax.fit_transform(self.norm_dataset)
        if data == None:
            self.invTrans_dataset = sax.inverse_transform(self.trans_dataset)
        else:
            self.invTrans_dataset = sax.inverse_transform(data)



    def norm(self, flag=1):
        n_max = max(self.dataset)
        if flag:
            self.dataset = np.array(self.dataset)
            print self.dataset.shape
            self.norm_dataset = self.dataset/n_max
        else:
            self.invTrans_dataset = self.invTrans_dataset*n_max

    def read(self):
        dataset = []
        with open('output.ou') as f: #aqui eu só carrego os valores do meu dataset
            for linha in f:
                linha = linha.strip()
                if linha:
                    valores = linha.split(',')
                    a,b = int(valores[0]), float(valores[1])
                    dataset.append(b)
        self.dataset = dataset[:] #gambito do welsu pra não passar por referência

        # exit = transform(300,300,dataset)
        # print exit
        # print len(exit[0])
np.set_printoptions(threshold='nan')
trans = Transform(300,300)
trans.read()
# trans.norm()
# trans.transform()
# trans.norm-(0)
# print trans.dataset
# print trans.invTrans_dataset[0]

sax = SymbolicAggregateApproximation(n_segments=300, alphabet_size_avg=300) 
trans.norm()   
aux = sax.fit_transform(trans.dataset)
aux1 = sax.inverse_transform(aux)
print trans.dataset
print aux
print aux1

