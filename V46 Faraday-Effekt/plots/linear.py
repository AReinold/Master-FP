import matplotlib.pyplot as plt
import numpy as np
import uncertainties.unumpy as unp
import scipy.constants as con
import scipy.optimize as opt
from scipy.optimize import curve_fit
from scipy import stats
from uncertainties import ufloat
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter,
                               AutoMinorLocator)

Bmax=414.47*10**(-3)


t1a, t2a, l = np.genfromtxt('GaAs1.txt', unpack=True)
t1b, t2b = np.genfromtxt('GaAs2.txt', unpack=True)
t1c, t2c = np.genfromtxt('GaAs3.txt', unpack=True)

l = l*10**(-6)
t1 = (t1a - t2a) * np.pi/180
t2 = (t1b - t2b) * np.pi/180
t3 = (t1c - t2c) * np.pi/180

#print('Theta [rad], N = 1.2e18: ', t1)
#print('Theta [rad], N = 2.8e18: ', t2)
#print('Theta [rad], hochrein: ', t3)

d1 = 1.36e-3# m
d2 = 1.296e-3 # m
d3 = 5.11e-3 # m

t1 = t1/d1
t2 = t2/d2
t3 = t3/d3

##############################################################################################################
def f(x, a, b):
    return a*x + b

tA = t1 - t3
tB = t2 - t3

params1, cov1 = curve_fit(f, (l*10**6)**2, tA)
err1 = np.sqrt(np.diag(cov1))

print('\nDifferenzen t1-t3:')
print('a = ', params1[0], r'\pm', err1[0])
print('b = ', params1[1], r'\pm', err1[1])

params2, cov2 = curve_fit(f, (l*10**6)**2, tB)
err2 = np.sqrt(np.diag(cov2))

print('\nDifferenzen t2-t3:')
print('a = ', params2[0], r'\pm', err2[0])
print('b = ', params2[1], r'\pm', err2[1])


ll = np.linspace(0.8, 7.2, 1000)

plt.plot((l*10**6)**2, tA, 'x', color='r', label=r'n-dotiertes GaAs, $N=1,,2\cdot10^{18}\mathrm{cm}^{-3}}$')
plt.plot((l*10**6)**2, tB, 'x', color='#2c5194', label=r'n-dotiertes GaAs, $N=2,8\cdot10^{18}\mathrm{cm}^{-3}}$')
plt.plot(ll, f(ll, *params1), '-', color='r', label=r'Fit $f(\lambda^2) = a_1\lambda^2 + b_1$, $N=1,2\cdot10^{18}\mathrm{cm}^{-3}}$')
plt.plot(ll, f(ll, *params2), '-', color='#2c5194', label=r'Fit $f(\lambda^2) = a_2\lambda^2 + b_2$, $N=2,8\cdot10^{18}\mathrm{cm}^{-3}}$')
plt.xlabel(r'$\lambda^2 \:/\:$µm')
plt.ylabel(r'$\frac{\Theta}{d} \:/\:$rad$\mathrm{m}^{-1}}$')
leg1 = plt.legend(loc='best', fancybox=False, fontsize='small', edgecolor='k')
leg1.get_frame().set_linewidth(0.3)

plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('GaAs2.pdf')
