#!/usr/bin/env python
# -*- coding: utf-8 -*-
import csv
import os
from shutil import copyfile
import knn_prediction as knn

def create_score_files():
    rootdir = 'saida/'
    for subdir, dirs, files in os.walk(rootdir):
        # print subdir,
        score_pips = []
        score_volca = []
        score_zigzag = []

        with open('new_saida/'+subdir[6:11]+'_scores'+'.csv', 'w') as csvfile:
                fieldnames = ['algorithm/points','15','20','25','30','35']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()

        for file in files:
            if (file.startswith('pips', 2,len(file)) or file.startswith('pips', 3,len(file))):
                if file.startswith('15',0,2):
                    copyfile(subdir+'/'+file,'output.ou')
                    score_pips.append(knn.main())
                if file.startswith('20',0,2):
                    copyfile(subdir+'/'+file,'output.ou')
                    score_pips.append(knn.main())
                if file.startswith('25',0,2):
                    copyfile(subdir+'/'+file,'output.ou')
                    score_pips.append(knn.main())
                if file.startswith('30',0,2):
                    copyfile(subdir+'/'+file,'output.ou')
                    score_pips.append(knn.main())
                if file.startswith('35',0,2):
                    copyfile(subdir+'/'+file,'output.ou')
                    score_pips.append(knn.main())
            if (len(score_pips) == 5):
                print "entrei pips"
                with open('new_saida/'+subdir[6:11]+'_scores'+'.csv', 'a') as csvfile:
                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                    writer.writerow({'algorithm/points': 'pips', '15': score_pips[0], '20': score_pips[1], '25': score_pips[2], '30': score_pips[3], '35': score_pips[4]})
                score_pips = []


            if (file.startswith('volca', 2,len(file)) or file.startswith('volca', 3,len(file))):
                if file.startswith('15',0,2):
                    copyfile(subdir+'/'+file,'output.ou')
                    score_volca.append(knn.main())
                if file.startswith('20',0,2):
                    copyfile(subdir+'/'+file,'output.ou')
                    score_volca.append(knn.main())
                if file.startswith('25',0,2):
                    copyfile(subdir+'/'+file,'output.ou')
                    score_volca.append(knn.main())
                if file.startswith('30',0,2):
                    copyfile(subdir+'/'+file,'output.ou')
                    score_volca.append(knn.main())
                if file.startswith('35',0,2):
                    copyfile(subdir+'/'+file,'output.ou')
                    score_volca.append(knn.main())
            if (len(score_volca) == 5):
                print "entrei volca"
                with open('new_saida/'+subdir[6:11]+'_scores'+'.csv', 'a') as csvfile:
                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                    writer.writerow({'algorithm/points': 'volca', '15': score_volca[0], '20': score_volca[1], '25': score_volca[2], '30': score_volca[3], '35': score_volca[4]})
                score_volca = []


            if (file.startswith('zigzag', 2,len(file)) or file.startswith('zigzag', 3,len(file))):
                if file.startswith('15',0,2):
                    copyfile(subdir+'/'+file,'output.ou')
                    score_zigzag.append(knn.main())
                if file.startswith('20',0,2):
                    copyfile(subdir+'/'+file,'output.ou')
                    score_zigzag.append(knn.main())
                if file.startswith('25',0,2):
                    copyfile(subdir+'/'+file,'output.ou')
                    score_zigzag.append(knn.main())
                if file.startswith('30',0,2):
                    copyfile(subdir+'/'+file,'output.ou')
                    score_zigzag.append(knn.main())
                if file.startswith('35',0,2):
                    copyfile(subdir+'/'+file,'output.ou')
                    score_zigzag.append(knn.main())
            if (len(score_zigzag) == 5):
                print "entrei zig"
                with open('new_saida/'+subdir[6:11]+'_scores'+'.csv', 'a') as csvfile:
                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                    writer.writerow({'algorithm/points': 'zigzag', '15': score_zigzag[0], '20': score_zigzag[1], '25': score_zigzag[2], '30': score_zigzag[3], '35': score_zigzag[4]})
                score_zigzag = []
create_score_files()