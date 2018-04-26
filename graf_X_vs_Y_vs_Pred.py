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
import make_output_file as mkof

def iterates_folder():
    if not os.path.exists("new_saida/"+"Y_vs_X_vs_Pred"):
        os.makedirs("new_saida/"+"Y_vs_X_vs_Pred")
    rootdir = 'entrada/'
    for subdir, dirs, files in os.walk(rootdir):
        # if not os.path.exists("new_saida/"+"Y_vs_X_vs_Pred/"+subdir[6:11]):
        #     os.makedirs("new_saida/"+"Y_vs_X_vs_Pred/"+subdir[6:11])
        for file in files:
        # if (file.startswith('100') and (not file.endswith('pdf') and not file.endswith('csv'))):
            # copyfile(subdir+'/'+file,'output.ou')
            mkof.trataArquivo(rootdir+file)
            x_test, y_test, pred = knn.main()
            print "executing hole dataset tests..."
            generate(x_test,y_test,pred,file,subdir)

def generate(x,y,pred,file, subdir):
    
    x = [str(i) for i in x]
    x = mdates.datestr2num(x)
    if (len(pred) > len(x)):
        pred = pred[:-1]

    hfmt = mdates.DateFormatter('%d/%m/%Y')
    fig, ax = plt.subplots()
    ax.xaxis.set_major_formatter(hfmt)

    plt.plot_date(x=x, y=y, fmt="k-", label='Real')
    plt.plot(x,pred,'g-',label='pred')

    plt.title("Data vs Valor vs Valor Predito")
    plt.xlabel("Data")
    plt.ylabel("Valores")

    plt.xticks(rotation=60)
    plt.tight_layout()
    plt.grid(True)
    # pdf = PdfPages('new_saida/Y_vs_X_vs_Pred/'+subdir[6:11]+'/'+file+'.pdf')
    pdf = PdfPages('new_saida/Y_vs_X_vs_Pred/'+file+'.pdf')
    # title(pontos+'pt_vs_original')
    pdf.savefig()
    close()
    pdf.close()


    
iterates_folder()