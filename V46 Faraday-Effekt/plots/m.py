import matplotlib.pyplot as plt
import numpy as np
import uncertainties.unumpy as unp
import scipy.constants as con
import scipy.optimize as opt
from scipy.optimize import curve_fit
from scipy import stats
from uncertainties import ufloat

# Effektive Masse
print('\n\nBerechnung der effektiven Masse:')
N1 = 1.2e18*10**(-6)
N2 = 2.8e18*10**(-6)

Bmax=414.47*10**(-3)
e0 = con.e
eps = con.epsilon_0
c = con.c
n = 3.3543
a1=ufloat(10.49*10**12, 4.17*10**12)
a2=ufloat(17.33*10**12, 6.43*10**12)

# a1 = ufloat(params1[0], err1[0])
# a2 = ufloat(params2[0], err2[0])

def m(a, N):
    return unp.sqrt((e0**3)/(8*np.pi**2*eps*c**3) * (N*Bmax)/n * 1/a)

# def m2(a, N):
#     return unp.sqrt(a*N*Bmax/(n*a))*con.m_e

mtheo = 0.067 # m_e
m1 = m(a1, N1)/con.m_e # m_e; N = 1.2e18
m2 = m(a2, N2)/con.m_e # m_e; N = 2.8e18

print('GaAs, N = 1.2e18: m* = ', m1)
print('GaAs, N = 2.8e18: m* = ', m2)
print('Theorie: ', mtheo)

# f=(unp.sqrt((e0**3)/(8*np.pi**2*eps*c**3)*(N2*Bmax)/(n)*(1)/(a2)))
# m1 = f/con.m_e # m_e; N = 1.2e18
# print(m1)
# m2 = m(a2, N2)/con.m_e # m_e; N = 2.8e18
#
# print('GaAs, N = 1.2e18: m* = ', m1)
# print('GaAs, N = 2.8e18: m* = ', m2)
#print('Theorie: ', mtheo)
