import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.optimize import curve_fit
from scipy.optimize import brentq
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy.stats import stats

I, Bauf, Bab = np.genfromtxt('eichung.txt', unpack=True)

def fit(x,a,b):
    return a*x+b

params, cov = curve_fit(fit, I, Bauf)
err = np.sqrt(np.diag(cov))

print('\nEichung:')
print('a = ', params[0], r'\pm', err[0])
print('b = ', params[1], r'\pm', err[1])

print('\n _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_')
a_fit=ufloat(183.320879, 7.8757597788)
b_fit=ufloat(-36.0164822, 27.8450161)
I_1=2.5
I_2=3.8
I_3=6.0
B = a_fit*I_3+b_fit
print(B)
print('\n _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_')


Ix = np.linspace(0, 6, 1000)

plt.plot(I, Bauf, 'C2x', label='$B$ aufsteigend')
plt.plot(I, Bab, 'C3x', label='$B$ absteigend')
plt.plot(Ix, fit(Ix, *params),'k-', label=r'Lineare Ausgleichsrechnung: $B(I) = aI+b$')

plt.xlabel(r"$I\:/\:$A")
plt.ylabel(r"$B\:/\:$mT")
plt.legend(loc="best")
plt.tight_layout()
plt.savefig('eichung.pdf')
plt.clf()
