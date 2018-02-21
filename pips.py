#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import gera_graficos as graf
import time

class Pips():
    def __init__(self,valor,n,data):
        self.valor = valor
        self.data = data
        self.n = n
        self.simplification = []
        self.dist = 0

    def distance(self,type,x1,x2,x3,y1,y2,y3):
        dist = 0
        if(type == 1): #se type = 1 fazemos distancia euclidiana
            dist = np.sqrt(np.power(x1-x2,2)+np.power(y1-y2,2))
            dist += np.sqrt(np.power(x2-x3,2)+np.power(y2-y3,2))
        if (type == 0):#se type diferente de 1 fazemos distancia vertical
            # dist = (y1+(y2-y1)*((x3-x1)/(x2-x1)))-y3
            dist = self.calc_distancia_vertical(x1,y1,x2,y2,x3,y3)
        if (type == 2):#se type iguala 2 fazemos a distancia euclidiana somada à distância vertical
            dist = np.sqrt(np.power(x1-x2,2)+np.power(y1-y2,2))
            dist += np.sqrt(np.power(x2-x3,2)+np.power(y2-y3,2))
            dist += self.calc_distancia_vertical(x1,y1,x2,y2,x3,y3)

        if (type == 3):#se type igual a 3 fazemos a distancia euclidiana com angulo
            vet12 = []
            vet13 = []
            vet32 = []
            vet31 = []
            vet12.append(x2-x1)
            vet12.append(y2-y1)
            vet13.append(x3-x1)
            vet13.append(y3-y1)
            vet31.append(x1-x3)
            vet31.append(y1-y3)
            vet32.append(x2-x3)
            vet32.append(y2-y3)
            ang = np.arccos((vet12[0]*vet13[0]+vet12[1]*vet13[1])/(np.sqrt(vet12[0]**2 + vet12[1]**2)*np.sqrt(vet13[0]**2 + vet13[1]**2)))
            dist = np.sqrt(np.power(x1-x2,2)+np.power(y1-y2,2))*ang
            ang = np.arccos((vet32[0]*vet31[0]+vet32[1]*vet31[1])/(np.sqrt(vet32[0]**2 + vet32[1]**2)*np.sqrt(vet31[0]**2 + vet31[1]**2)))
            dist += np.sqrt(np.power(x2-x3,2)+np.power(y2-y3,2))*ang

        return dist

    def bigger_distance_point(self, b, e): #b = inicio/begin e = fim/end
        maior = 0
        maior_distancia = 0
        distancia = 0
        for i, val in enumerate(self.valor[b:e]):
            dist = self.distance(1,self.data[b],self.data[i+b],self.data[e],self.valor[b],self.valor[i+b],self.valor[e])
            # print i, dist
            # print maior, maior_distancia
            if (dist > maior_distancia):
                maior = i+b
                maior_distancia = dist
        # print "////////////////////////////////////"
        return maior, maior_distancia

    def calc_distancia_vertical(self,x_begin,y_begin,x_pip,y_pip,x_end,y_end): #função que calcula reta que liga os dois pontos mais próximos da simplificação
    	m = (float(y_end-y_begin))/(float(x_end-x_begin))
    	a = -m*float(x_begin)+float(y_begin)

        y_calc = m*x_pip+a
        distancia_vertical = abs(y_pip-y_calc)
    	return distancia_vertical

    def insert_auxiliar_list(self, list, pip, i, f, dist):
        celula = []
        celula.append(pip)
        celula.append(i)
        celula.append(f)
        celula.append(dist)
        list.append(celula)
        return list

    def search_biggest_auxiliar_list(self,list):
        indice_maior = 0
        maior = 0
        i_aux = 0
        for i, val in enumerate(list):
            if(val[3] > maior):
                i_aux = i
                maior = val[3]
                indice_maior = val[0]


        return indice_maior, i_aux, maior


    def calc_simplification(self, i, f):
        aux_list = [] #cria lista auxiliar que guarda pips não utilizados
        self.simplification.append(i) #coloca os 2 primeiros pips na simplificação
        self.simplification.append(f)

        for j in range(0,self.n-2): #for que obtém a quantidade de pontos pedidos

            old_pip, indice_old_pip, dist_old_pip = self.search_biggest_auxiliar_list(aux_list) #procura o maior pip na lista auxiliar
            pip, dist_pip = self.bigger_distance_point(i, f) #calcula o pip atual

            if(dist_pip < dist_old_pip or f == i): #verifica qual dos 2 é maior e se ainda existe algum número entre os 2 valores
                self.simplification.append(old_pip) #se o anterior for maior ele é colocado na lista de simplificação
                celula = aux_list[indice_old_pip] #linha adicional
                aux_list.pop(indice_old_pip) #é tirado da lista de auxiliares
                aux_list = self.insert_auxiliar_list(aux_list, pip, i, f, dist_pip) #colocamos o pip atual na lista de auxiliares

                pip = old_pip #para achar-mos os novos pips da esquerda e direita substituímos
                i = celula[1]
                f = celula[2]

            else:
                self.simplification.append(pip) #se o de agora for maior ele só é adicionado a lista de simplificação

            # print i,pip,f
            # print "Aux: ",
            # for c in aux_list:
            #     print c[0],
            # print ""

            pip_esq, dist_pip_esq = self.bigger_distance_point(i, pip) #pegamos os maiores da esquerda e da direita
            pip_dir, dist_pip_dir = self.bigger_distance_point(pip, f)

            if(dist_pip_esq > dist_pip_dir): #comparo pra ver qual dos dois pips é maior
                aux_list = self.insert_auxiliar_list(aux_list, pip_dir, pip, f, dist_pip_dir) #estou guardando na lista auxiliar o ponto que não foi escolhido como pip, neste caso o pip_dir
                f = pip
            else:
                aux_list = self.insert_auxiliar_list(aux_list, pip_esq, i, pip, dist_pip_esq) #estou guardando na lista auxiliar o ponto que não foi escolhido como pip, neste caso o pip_esq
                i = pip

        return 0

def trataValores(valores): #transforma os literais em valores inteiro e float, respectivamente, pra uso posterior
    return int(valores[0]), float(valores[1])

def main(n, W_data, W_valor):
    # W_data = []
    # W_valor = []
    # with open('output.ou') as f: #inicializa os valores de W a partir do arquivo de entrada
    #     for linha in f:
    #         linha = linha.strip()
    #         if linha:
    #             valores = linha.split(',')
    #             x,y = trataValores(valores)
    #             W_data.append(x)
    #             W_valor.append(y)
    W_data_aux = []
    for i, val in enumerate(W_data):
        W_data_aux.append(i)


    start_time = time.time()
    obj = Pips(W_valor, n, W_data_aux)
    obj.calc_simplification(0, len(W_valor)-1)
    obj.simplification.sort()
    simpl = []
    for i, val in enumerate(obj.simplification):
        cel = []
        cel.append(W_data[val])
        cel.append(W_valor[val])
        simpl.append(cel)
    temp = time.time() - start_time
    print "TEMPO PIPS:",temp
    return simpl, W_data, W_valor, temp
#####################################################
