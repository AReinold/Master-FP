import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.optimize import curve_fit
from scipy.optimize import brentq
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy.stats import stats
#-------------------- a2--------------------------------------------------------
print('Messdaten 2:')
f2, Ua2 = np.genfromtxt('v2.txt', unpack=True)

Ua2 = Ua2*10**(-3)
U_0=3 # volt

f_log2 = np.log(f2)
V_log2 = np.log(Ua2/U_0)
V_log2 = np.absolute(V_log2)

V_02 = np.mean(V_log2[:7])

print('V_02:',np.exp(V_02))
print(V_02)
# lineare Regression
def fit(x, a, b):
    return x*a+b

ParamsII, CovarianceII = curve_fit(fit, f_log2[11:17], V_log2[11:17])
i2 = np.linspace(13, 14.2, 10000)
ErrorsII = np.sqrt(np.diag(CovarianceII))
a2 = ufloat(ParamsII[0], ErrorsII[0])
b2 = ufloat(ParamsII[1], ErrorsII[1])
print('a2:', a2)
print('b2:', b2)
v2= unp.exp((np.log(V_02/np.sqrt(2))-b2)/a2)
print('Frequenz:', v2)

plt.plot(f_log2[:7], V_log2[:7], 'C1.', label='konstante Messwerte unterhalb der Grenzfrequenz')
plt.plot(f_log2[8:10], V_log2[8:10], 'k.')
plt.plot(f_log2[11:17], V_log2[11:17], 'C2.', label='Messwerte des Verstärkungsverlaufs')
plt.plot(f_log2[18:], V_log2[18:], 'k.', label='ignorierte Messwerte')

plt.plot(i2, fit(i2, *ParamsII), 'C0-', label='lineare Ausgleichsrechnung')
#plt.ylim(4, 5)
plt.xlabel(r"$ln(\nu)\:/\:ln$(Hz)")
plt.ylabel(r"$ln(V')$")
plt.legend(loc="best")
plt.tight_layout()
plt.savefig('A2.pdf')
plt.clf()
print('V*v', V_02*v2)
