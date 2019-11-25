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

f, U = np.genfromtxt('V2.txt', unpack = True)
f1, phi = np.genfromtxt('phi1.txt', unpack = True)
#plt.yscale('log')
#plt.xscale('log')
plt.show()
#f_log=np.log(f)
#U_log=np.log(U)
plt.plot(f_log,1/U_log,'r.',label='Messwerte')
def fx(x,m,b):
    return x*m+b
ParamsI, CovarianceI = curve_fit(fx, f_log[7:], U_log[7:])
i1 = np.linspace(11, 14, 1000000)
ErrorsI = np.sqrt(np.diag(CovarianceI))
m = ufloat(ParamsI[0], ErrorsI[0])
b = ufloat(ParamsI[1], ErrorsI[1])

plt.plot(i1, fx(i1, *ParamsI), 'b-', label='linear regression')
#############################################################
#plt.plot(f1,phi,'r.',label='Messwerte')
#plt.xscale('log')
#plt.yscale('log')
plt.show()
