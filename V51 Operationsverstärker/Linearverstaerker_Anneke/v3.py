import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.optimize import curve_fit
from scipy.optimize import brentq
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy.stats import stats
#-------------------- a2--------------------------------------------------------
print('Messdaten 3:')
f3, Ua3 = np.genfromtxt('v3.txt', unpack=True)

Ua3 = Ua3*10**(-3)
U_0=3 # volt

f_log3 = np.log(f3)
V_log3 = np.log(Ua3/U_0)
V_log3 = np.absolute(V_log3)
V_03 = np.mean(V_log3[:4])

print('V_03:',np.exp(V_03))
print(V_03)
# lineare Regression
def fit(x, a, b):
    return x*a+b

ParamsIII, CovarianceIII = curve_fit(fit, f_log3[5:12], V_log3[5:12])
i3 = np.linspace(6.9, 8.1, 10000)
ErrorsIII = np.sqrt(np.diag(CovarianceIII))
a3 = ufloat(ParamsIII[0], ErrorsIII[0])
b3 = ufloat(ParamsIII[1], ErrorsIII[1])
print('a3:', a3)
print('b3:', b3)
v3= unp.exp((np.log(V_03/np.sqrt(2))-b3)/a3)
print('Frequenz:', v3)
plt.plot(f_log3[0:4], V_log3[0:4], 'C1.', label='konstante Messwerte unterhalb der Grenzfrequenz')
plt.plot(f_log3[5:12], V_log3[5:12], 'C2.', label='Messwerte des Verstärkungsverlaufs')
plt.plot(f_log3[12:], V_log3[12:], 'k.', label='ignorierter Messwert')
plt.plot(i3, fit(i3, *ParamsIII), 'C0-', label='lineare Ausgleichsrechnung')
#plt.ylim(4, 5)
plt.xlabel(r"$ln(\nu)\:/\:ln$(Hz)")
plt.ylabel(r"$ln(V')$")
plt.legend(loc="best")
plt.tight_layout()
plt.savefig('A3.pdf')
plt.clf()
print('V*v', V_03*v3)
