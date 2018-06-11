#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tslearn.piecewise import PiecewiseAggregateApproximation
from tslearn.piecewise import SymbolicAggregateApproximation

from tslearn.generators import random_walks
from tslearn.preprocessing import TimeSeriesScalerMeanVariance
import numpy

def trataValores(valores): #transforma os literais em valores inteiro e float, respectivamente, pra uso posterior
    return int(valores[0]), float(valores[1]) 

def transform(n_paa, n_sax, dataset):
    paa = PiecewiseAggregateApproximation(n_segments=n_paa)
    paa_dataset = paa.fit_transform(dataset)
    sax = SymbolicAggregateApproximation(n_segments=n_paa, alphabet_size_avg=n_sax)    
    return sax.fit_transform(dataset)


def invers_transform(n_paa, n_sax, dataset):
    pass

if __name__ == '__main__':
    dataset = []
    with open('output.ou') as f: #aqui eu só carrego os valores do meu dataset
        for linha in f:
            linha = linha.strip()
            if linha:
                valores = linha.split(',')
                a,b = trataValores(valores)
                dataset.append(b)

    n_max = max(dataset)
    dataset = numpy.array(dataset)
    dataset = dataset/n_max
    print dataset
    exit = transform(50,30,dataset)
    print exit
    print len(exit[0])
    

