import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np
import uncertainties.unumpy as unp
from uncertainties.umath import sqrt
from uncertainties import ufloat
import math
z, B = np.genfromtxt('hallsonde.txt', unpack=True)
#def f(x, m,b):
#    return m*1/x+b
#params, cov = curve_fit(f, t, a)
#m= params[0]
#b=params[1]
#dm = np.sqrt(cov[0][0])
#db = np.sqrt(cov[1][1])
#x=np.linspace(70, 300, 1000)

plt.plot(z, B, 'rx', label='Messwerte')
#plt.plot(1/x, f(x, m, b), 'g-', label='Ausgleichsgerade')

plt.xlabel(r"$z \:/\: \mathrm{mm}$")
plt.ylabel(r"$-B \:/\: \mathrm{mT}$")
#plt.ylim(6.5, 17)

# print('Parameter: ', params, '\nFehler: ', np.sqrt(np.diag(cov)))
plt.grid()
plt.legend(loc='best')
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('hall.pdf')
