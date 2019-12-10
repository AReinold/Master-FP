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

z, counts = np.genfromtxt('detektorscan.txt', unpack = True)
plt.plot(z,counts,'r.',label='Messwerte')
def fx(x,m,b):
    return m*x**b
ParamsI, CovarianceI = curve_fit(fx, f[6:12], U[6:12])
i1 = np.linspace(97000, 397000, 1000000)
ErrorsI = np.sqrt(np.diag(CovarianceI))
m = ufloat(ParamsI[0], ErrorsI[0])
b = ufloat(ParamsI[1], ErrorsI[1])
#print("Verstärker 4")
#print("m,b")
#print(m,b)
plt.plot(i1, fx(i1, *ParamsI), 'b-', label='Fit')
#plt.xlim(4.4,13)
#plt.ylim(5.7,6)
plt.ylabel(r'Ausgangsspannung $[\si{\mV}]$',fontsize = 12)
plt.xlabel(r'Frequenz  $[\si{\Hz}]$',fontsize = 12)
plt.legend()
#############################################################
#plt.plot(f1,phi,'r.',label='Messwerte')
#plt.xscale('log')
#plt.yscale('log')
plt.show()
