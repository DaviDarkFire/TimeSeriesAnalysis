#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division
import csv
import os


def generate_csv(algorithm_name,n):
    lista_media = []
    for i in range(0,20):
        lista_media.append(0.0)

    with open('new_saida/'+algorithm_name+'.csv', 'w') as csvfile:
        fieldnames = ['market/points','5','10','15','20','25','30','35','40','45','50','55','60','65','70','75','80','85','90','95','100']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
    rootdir = 'saida/'
    for subdir, dirs, files in os.walk(rootdir):
        for file in files:
            if (file.endswith(".csv")):
                archive = csv.reader(open(subdir+"/"+file), delimiter = ',')
                lista = []
                for row in archive:
                    lista.append(row[n])

                for i in range(0,20):
                    lista_media[i] = float(lista[i+1])+lista_media[i]

                with open('new_saida/'+algorithm_name+'.csv', 'a') as csvfile:
                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                    writer.writerow({'market/points': subdir, '5': lista[1], '10': lista[2], '15': lista[3], '20': lista[4], '25': lista[5], '30': lista[6], '35': lista[7], '40': lista[8], '45': lista[9], '50': lista[10], '55': lista[11], '60': lista[12],'65': lista[13], '70': lista[14], '75': lista[15], '80': lista[16], '85': lista[17], '90': lista[18], '95': lista[19], '100': lista[20]})
    for j in range(0,20):
        lista_media[j] = lista_media[j]/48
    with open('new_saida/'+algorithm_name+'.csv', 'a') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow({'market/points': 'Média', '5': lista_media[0], '10': lista_media[1], '15': lista_media[2], '20': lista_media[3], '25': lista_media[4], '30': lista_media[5], '35': lista_media[6], '40': lista_media[7], '45': lista_media[8], '50': lista_media[9], '55': lista_media[10], '60': lista_media[11],'65': lista_media[12], '70': lista_media[13], '75': lista_media[14], '80': lista_media[15], '85': lista_media[16], '90': lista_media[17], '95': lista_media[18], '100': lista_media[19]})

generate_csv("saida_pips",2)
generate_csv("saida_volca",4)
generate_csv("saida_zigzag",6)
