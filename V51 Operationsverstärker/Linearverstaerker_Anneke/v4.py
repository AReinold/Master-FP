import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.optimize import curve_fit
from scipy.optimize import brentq
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy.stats import stats

#-------------------- a2--------------------------------------------------------
print('Messdaten 4:')
f4, Ua4 = np.genfromtxt('v4.txt', unpack=True)

U_0=3 # volt

f_log4 = np.log(f4)
V_log4 = np.log(Ua4/U_0)
V_04 = np.mean(V_log4[:7])

print('V_04:',np.exp(V_04))
print(V_04)
# lineare Regression
def fit(x, a, b):
    return x*a+b

ParamsIV, CovarianceIV = curve_fit(fit, f_log4[8:], V_log4[8:])
i4 = np.linspace(10.7, 14, 10000)
ErrorsIV = np.sqrt(np.diag(CovarianceIV))
a4 = ufloat(ParamsIV[0], ErrorsIV[0])
b4 = ufloat(ParamsIV[1], ErrorsIV[1])
print('a4:', a4)
print('b4:', b4)
v4= unp.exp((np.log(V_04/np.sqrt(2))-b4)/a4)
print('Frequenz:', v4)
plt.plot(f_log4[0:7], V_log4[0:7], 'C1.', label='konstante Messwerte unterhalb der Grenzfrequenz')
plt.plot(f_log4[8:], V_log4[8:], 'C2.', label='Messwerte des Verstärkungsverlaufs')
plt.plot(i4, fit(i4, *ParamsIV), 'C0-', label='lineare Ausgleichsrechnung')
#plt.ylim(4, 5)
plt.xlabel(r"$ln(\nu)\:/\:ln$(Hz)")
plt.ylabel(r"$ln(V')$")
plt.legend(loc="best")
plt.tight_layout()
plt.savefig('A4.pdf')
plt.clf()
print('V*v', V_04*v4)
