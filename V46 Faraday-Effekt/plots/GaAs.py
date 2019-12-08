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

t1a, t2a, l = np.genfromtxt('GaAs1.txt', unpack=True)
t1b, t2b = np.genfromtxt('GaAs2.txt', unpack=True)
t1c, t2c = np.genfromtxt('GaAs3.txt', unpack=True)

l = l*10**(-6)
t1 = (t1a - t2a) * np.pi/180
t2 = (t1b - t2b) * np.pi/180
t3 = (t1c - t2c) * np.pi/180

print('Theta [rad], N = 1.2e18: ', t1)
print('Theta [rad], N = 2.8e18: ', t2)
print('Theta [rad], hochrein: ', t3)

d1 = 1.36e-3# m
d2 = 1.296e-3 # m
d3 = 5.11e-3 # m

t1 = t1/d1
t2 = t2/d2
t3 = t3/d3

print('\nTheta/d [rad/m], N = 1.2e18:', t1)
print('Theta/d [rad/m], N = 2.8e18:', t2)
print('Theta/d [rad/m], hochrein:', t3)

# Plot und Labels/ Legende
plt.plot((l*10**6)**2, t1, 'x', color='C2', label=r'n-dotiertes GaAs, $N=1,2\cdot10^{18}\mathrm{cm}^{-3}$')
plt.plot((l*10**6)**2, t2, 'x', color='C3', label=r'n-dotiertes GaAs, $N=2,8\cdot10^{18}\mathrm{cm}^{-3}$')
plt.plot((l*10**6)**2, t3, 'x', color='C0', label=r'GaAs, hochrein')
plt.xlabel(r'$\lambda^2 \:/\:$µm')
plt.ylabel(r'$\frac{\Theta}{d} \:/\:$rad$\mathrm{m}^{-1}$')
leg1 = plt.legend(loc='best', fancybox=False, fontsize='small', edgecolor='k')
# in matplotlibrc leider (noch) nicht möglich
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('GaAs.pdf')
##############################################################################################################
