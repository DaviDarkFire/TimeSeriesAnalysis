#!/usr/bin/env python
# -*- coding: utf-8 -*-

def main(i, dataset_name,od_pips, od_volca, od_zigzag):
    saida_pips = open("saida/"+dataset_name+"/"+str(i)+"_pips","w")
    saida_volca = open("saida/"+dataset_name+"/"+str(i)+"_volca","w")
    saida_zigzag = open("saida/"+dataset_name+"/"+str(i)+"_zigzag","w")
    for i, val in enumerate(od_pips):
        saida_pips.write(str(val[0]))
        saida_pips.write(',')
        saida_pips.write(str(val[1]))
        saida_pips.write('\n')

    for i, val in enumerate(od_volca):
        saida_volca.write(str(val[0]))
        saida_volca.write(',')
        saida_volca.write(str(val[1]))
        saida_volca.write('\n')

    for i, val in enumerate(od_zigzag):
        saida_zigzag.write(str(val[0]))
        saida_zigzag.write(',')
        saida_zigzag.write(str(val[1]))
        saida_zigzag.write('\n')

    saida_pips.close()
    saida_volca.close()
    saida_zigzag.close()
