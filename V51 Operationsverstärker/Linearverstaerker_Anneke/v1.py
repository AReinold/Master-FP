import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.optimize import curve_fit
from scipy.optimize import brentq
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy.stats import stats
#-------------------- a1--------------------------------------------------------
print('Messdaten 1:')
f1, Ua1 = np.genfromtxt('v1.txt', unpack=True)

Ua1 = Ua1*10**(-3)
U_0=3 # volt

f_log = np.log(f1)

V_log = np.log(Ua1/U_0)
V_log = np.absolute(V_log)

V_0 = np.mean(V_log[:6])

print('V_0:',np.exp(V_0))
print(V_0)
# lineare Regression
def fit(x, a, b):
    return x*a+b

ParamsI, CovarianceI = curve_fit(fit, f_log[17:], V_log[17:])
i = np.linspace(13.1, 14, 10000)
ErrorsI = np.sqrt(np.diag(CovarianceI))
a = ufloat(ParamsI[0], ErrorsI[0])
b = ufloat(ParamsI[1], ErrorsI[1])
print('a:', a)
print('b:', b)
v= unp.exp((np.log(V_0/np.sqrt(2))-b)/a)
print('Frequenz:', v)
plt.plot(f_log[:6], V_log[:6], 'C1.', label='konstante Messwerte unterhalb der Grenzfrequenz')
plt.plot(f_log[7:], V_log[7:], 'C2.', label='Messwerte des Verstärkungsverlaufs')
plt.plot(f_log[7:16], V_log[7:16], 'k.', label='ignorierte Messwerte')
plt.plot(i, fit(i, *ParamsI), 'C0-', label='lineare Ausgleichsrechnung')
#plt.ylim(4, 5)

plt.xlabel(r"$ln(\nu)\:/\:ln$(Hz)")
plt.ylabel(r"$ln(V')$")
plt.legend(loc="best")
plt.tight_layout()
plt.savefig('A1.pdf')
plt.clf()
print('V*v', V_0*v)
