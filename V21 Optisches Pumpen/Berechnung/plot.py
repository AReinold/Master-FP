import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np
import uncertainties.unumpy as unp
from uncertainties.umath import sqrt
from uncertainties import ufloat
import math
f, B1, B2 = np.genfromtxt('resonanz.txt', unpack=True)
#def f(x, m,b):
#    return m*1/x+b
#params, cov = curve_fit(f, t, a)
#m= params[0]
#b=params[1]
#dm = np.sqrt(cov[0][0])
#db = np.sqrt(cov[1][1])
#x=np.linspace(70, 300, 1000)

plt.plot(f, B1, 'r-', label='B1')
plt.plot(f, B2, 'g-', label='B2')

plt.xlabel(r"$T^{-1}$ in $\mathrm{K}^{-1}$")
plt.ylabel(r"$\alpha\cdot 10^{-6}$ in $\mathrm{K}^{-1}$")
#plt.ylim(6.5, 17)

# print('Parameter: ', params, '\nFehler: ', np.sqrt(np.diag(cov)))
plt.legend(loc='best')
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('resonanz.pdf')
