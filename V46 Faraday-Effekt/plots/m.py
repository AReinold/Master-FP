import matplotlib.pyplot as plt
import numpy as np
import uncertainties.unumpy as unp
import scipy.constants as con
import scipy.optimize as opt
from scipy.optimize import curve_fit
from scipy import stats
from uncertainties import ufloat


Bmax=414.47*10**(-3)
e0 = con.e
eps = con.epsilon_0
c = con.c
n = 3.3543
a1=16
a2=ufloat(4.1,29.7)
# a1 = ufloat(-16,12.9)
# a2 = ufloat(90.99,56.33)
N1 = 1.2e18
N2 = 2.8e18

f=(unp.sqrt((e0**3)/(8*np.pi**2*eps*c**3)*(N2*Bmax)/(n)*(1)/(a2)))
m1 = f/con.m_e # m_e; N = 1.2e18
print(m1)
# m2 = m(a2, N2)/con.m_e # m_e; N = 2.8e18
#
# print('GaAs, N = 1.2e18: m* = ', m1)
# print('GaAs, N = 2.8e18: m* = ', m2)
#print('Theorie: ', mtheo)
