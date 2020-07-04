'''This program is for --
    1. Reading & seperating -ve & +ve parts of the data.
    2. Plotting it then fitting with symmetric & antisymmetric Lorentzians
        In the course of fitting -
        i. to extract a) H0, ∂H, D, L
        ii. to write the values in a file and then analyze from that'''

#matplotlib inline
import matplotlib.pyplot as plt
import scipy.optimize as opt
import numpy as np
import array as arr
import itertools
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import scipy.fftpack
from numpy import *
from scipy.optimize import curve_fit
import os
import csv
import pandas as pd

# Normalize the data attributes for the Iris dataset.
from sklearn.datasets import load_iris
from sklearn import preprocessing
########################################################
font = {'family' : 'arial',
        'weight' : 'normal',
        'size'   : 12}

matplotlib.rc('font', **font)
##########Importing data################################
os.chdir('/Users/bipulkumar/Google Drive/Coding Related/Data_Science/STFMR_DATA/Rh_Py/Freq_Vary/Analysed')
filelist=[]
#Hs=[]
#Fs=[]
Freqs=[3,4,5,6,7,8,9,10]
#Angles=range(3,11,1)
#Angles=[0,10,20,30,40,50,70,100,110,120,130,140,150,160,170,180,190,200,210,220,230,240,250,260,290,300,310,320,330,340,350,360]
##print(list(Angles))
fig = plt.figure()
ax1 = fig.add_subplot(111)
colors = itertools.cycle(["red", "green", "blue","purple","cyan","yellow","magenta","black","lime","maroon","navy", "olive","teal","gray"])
n='GHz'
for i in Freqs:
    filelist.append("Rh_Py0_10dBm_90Th_45Ph_0Be_0Volts_GHz-%s.txt" %i)
    for item in filelist:
        f=np.genfromtxt(item,dtype=float,skip_header=1) #for txt file
    #    N=200
        H=f[5:,0]*10000
        F=f[5:,1]*1e6
    ax1.plot(H, F,'-', color=next(colors),label='%s %s' %(i,n),markersize=6,linewidth=3)
#ax1.set_title("All Angles 20dB")
ax1.set_xlabel("External magnetic field (Oe)",size=24)
ax1.set_ylabel("STFMR signal (µV)",size=24)
ax1.set_ylim(-125,80)
ax1.tick_params(axis='both', which='major', labelsize=20)
plt.rcParams.update({'font.size': 16})
leg = ax1.legend(fontsize=15, ncol=4,labelspacing=0.05,handlelength=1,handletextpad=0.1,loc="lower left")
plt.savefig("Rh5Py5 all frequencies together 45º @10dB.pdf",bbox_inches='tight')
#ax1.grid()
plt.show()
##f=np.genfromtxt('Sample3_OnThePad_RIM0.5to0V_place2Changed-1.csv',dtype=float,skip_header=2,delimiter=',')
##print(f['x'])
#import pandas as pd
#df = pd.read_csv('Sample3_OnThePad_RIM0.5to0V_place2Changed-1.csv')
#print(df[:])
