#!/usr/bin/env python
# -*- coding: utf-8 -*-
import csv
import os
import knn_prediction as knn
from shutil import copyfile
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.backends.backend_pdf import PdfPages
from pylab import *

def iterates_folder():
    if not os.path.exists("new_saida/"+"Y_vs_X_vs_Pred"):
        os.makedirs("new_saida/"+"Y_vs_X_vs_Pred")
    rootdir = 'saida/'
    for subdir, dirs, files in os.walk(rootdir):
        if not os.path.exists("new_saida/"+"Y_vs_X_vs_Pred/"+subdir[6:11]):
            os.makedirs("new_saida/"+"Y_vs_X_vs_Pred/"+subdir[6:11])
        for file in files:
            if (file.startswith('pips', 2,len(file)) or file.startswith('pips', 3,len(file)) or file.startswith('volca', 2,len(file)) or file.startswith('volca', 3,len(file))  or file.startswith('zigzag', 2,len(file)) or file.startswith('zigzag', 3,len(file))):
                copyfile(subdir+'/'+file,'output.ou')
                x_test, y_test, pred = knn.main()
                generate(x_test,y_test,pred,file,subdir)

def generate(x_test,y_test,pred,file, subdir):
    x_test_aux = []
    for i in x_test:
        x_test_aux.append(str(i[0]))
    x_test_aux = mdates.datestr2num(x_test_aux)
    y_test = y_test.tolist()
    pred = pred.tolist()
    x_test_aux.sort()
    hfmt = mdates.DateFormatter('%d/%m/%Y')
    fig, ax = plt.subplots()
    ax.xaxis.set_major_formatter(hfmt)

    plt.plot_date(x=x_test_aux, y=y_test, fmt="k-", label='Real')
    plt.plot(x_test_aux,pred,'g-',label='pred')

    plt.title("Data vs Valor vs Valor Predito")
    plt.xlabel("Data")
    plt.ylabel("Valores")

    plt.xticks(rotation=60)
    plt.tight_layout()
    plt.grid(True)
    pdf = PdfPages('new_saida/Y_vs_X_vs_Pred/'+subdir[6:11]+'/'+file)
    # title(pontos+'pt_vs_original')
    pdf.savefig()
    close()
    pdf.close()


    
iterates_folder()