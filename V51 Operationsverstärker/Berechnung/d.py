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

f, U = np.genfromtxt('e.txt', unpack = True)

#f_log=np.log(f)
#U_log=np.log(U)
plt.yscale('log')
plt.xscale('log')
plt.plot(f,U,'r.',label='Messwerte')
#plt.plot(f_log,U_log,'r.',label='Messwerte')
def fx(x,m,b):
    return np.exp(np.log(x)*m+b)
ParamsI, CovarianceI = curve_fit(fx, f[1:6], U[1:6])
#ParamsI, CovarianceI = curve_fit(fx, f_log, U_log)
i1 = np.linspace(50, 2500, 1000)
ErrorsI = np.sqrt(np.diag(CovarianceI))
m = ufloat(ParamsI[0], ErrorsI[0])
b = ufloat(ParamsI[1], ErrorsI[1])
print(m,b)
plt.plot(i1, fx(i1, *ParamsI), 'b-', label='Lineare Regression')
plt.ylabel(r"$U_\text{A} \:/\:$mV")
plt.xlabel(r"$\nu \:/\:$Hz")
plt.legend()
plt.savefig('diffe.pdf')
#plt.xscale('log')
#plt.yscale('log')
plt.show()
