import matplotlib.pyplot as plt
import numpy as np
import math
import cmath as cm
import pandas as pd
from scipy.optimize import curve_fit
from scipy.optimize import brentq
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy.stats import stats
plt.rcParams['text.usetex'] = True
plt.rcParams['text.latex.unicode'] = True
plt.rcParams['text.latex.preamble'] = [r'\usepackage{amsmath}']
plt.rcParams['text.latex.preamble'] = [r'\usepackage{siunitx}']

z, counts = np.genfromtxt('Detectorscan.uxd', unpack = True)
plt.plot(z,counts,'r.',label='Messwerte')
def fx(x,a,b,c):
    return a*np.exp(-(x-b)**2/(2*c**2))
a=1100000
b=0
c=0.05
ParamsI, CovarianceI = curve_fit(fx, z, counts, p0=[1100000,0,0.05])
i1 = np.linspace(-0.15, 0.15, 1000)
#i1 = np.linspace(-0.15, 0.15, 1000)
ErrorsI = np.sqrt(np.diag(CovarianceI))
a = ufloat(ParamsI[0], ErrorsI[0])
b = ufloat(ParamsI[1], ErrorsI[1])
c = ufloat(ParamsI[2], ErrorsI[2])
#print("Verstärker 4")
#print("m,b")
print(a,b,c)
plt.plot(i1, fx(i1, *ParamsI), 'b-', label='Fit')
#plt.plot(i1,fx(i1,a,b,c),'b-')
#plt.xlim(4.4,13)
#plt.ylim(5.7,6)
plt.ylabel(r'Intensität',fontsize = 12)
plt.xlabel(r'$z$-Position  $[\si{\mm}]$',fontsize = 12)
plt.legend()
fuck=fx(i1,*ParamsI)
max_f=max(fuck)
HM=max_f/2
h=[]
y=-0.15
j=0
for i in range(1000):
    if fx(y,*ParamsI)>=HM:
        h=np.append(h,y)
        j=j+1
    y=y+0.0003
print(np.abs(h[0])+np.abs(h[j-1]))

#############################################################
#plt.plot(f1,phi,'r.',label='Messwerte')
#plt.xscale('log')
#plt.yscale('log')
plt.show()
