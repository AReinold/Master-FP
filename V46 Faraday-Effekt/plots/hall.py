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

################################################################################

z, B = np.genfromtxt('hallsonde.txt', unpack=True)
z2, B2 = np.genfromtxt('hallsonde2.txt', unpack=True)
def Bfit(x, a, b, c, d, e):
    return a*x**4 + b*x**3 + c*x**2 + d*x + e

paramsB, covB = curve_fit(Bfit, z2, B2)
errB = np.sqrt(np.diag(covB))

print('\nB-Feld-Messung:')
print('a = ', paramsB[0], r'\pm', errB[0])
print('b = ', paramsB[1], r'\pm', errB[1])
print('c = ', paramsB[2], r'\pm', errB[2])
print('d = ', paramsB[3], r'\pm', errB[3])
print('e = ', paramsB[4], r'\pm', errB[4])

zz = np.linspace(117, 142, 1000)

# Eistellungen des Plots
#for axis in ['top','bottom','left','right']:
#  ax.spines[axis].set_linewidth(0.3)

# Plot und Labels/ Legende
plt.plot(z, B, 'kx', label='Messwerte')
plt.plot(zz, Bfit(zz, *paramsB), '-', color='C2', label=r'Fit $B(z) = az^4 + bz^3 + cz^2 + dz + e$')
#ax.plot(11.83622352553338, Bfit(11.83622352553338, *paramsB), 'r.', label=r'$Bmax = 423.32$ mT')
plt.xlabel(r'$z \:/\:$mm')
plt.ylabel(r'$B \:/\:$mT')
leg1 = plt.legend(loc='best', fancybox=False, fontsize='small', edgecolor='k')

# Einstellung der Achsen
plt.xlim(95, 165)
plt.ylim(0, 420)
# in matplotlibrc leider (noch) nicht möglich
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('hall.pdf')

# def f(x, a, b):
#     return a*x + b
#
# tA = t1 - t3
# tB = t2 - t3
#
# params1, cov1 = curve_fit(f, (l*10**6)**2, tA)
# err1 = np.sqrt(np.diag(cov1))
#
# print('\nDifferenzen t1-t3:')
# print('a = ', params1[0], r'\pm', err1[0])
# print('b = ', params1[1], r'\pm', err1[1])
#
# params2, cov2 = curve_fit(f, (l*10**6)**2, tB)
# err2 = np.sqrt(np.diag(cov2))
#
# print('\nDifferenzen t2-t3:')
# print('a = ', params2[0], r'\pm', err2[0])
# print('b = ', params2[1], r'\pm', err2[1])
#
#
# ll = np.linspace(0.8, 7.2, 1000)
#
# # Eistellungen des Plots
# fig = plt.figure()
# ax = fig.add_axes([0.12, 0.13, 0.8, 0.83])
# for axis in ['top','bottom','left','right']:
#   ax.spines[axis].set_linewidth(0.3)
#
# # Plot und Labels/ Legende
# ax.plot((l*10**6)**2, tA, 'x', color='r', label=r'n-dotiertes $\ce{GaAs}$, $N=\SI{1.2e18}{\centi\meter^{-3}}$')
# ax.plot((l*10**6)**2, tB, 'x', color='#2c5194', label=r'n-dotiertes $\ce{GaAs}$, $N=\SI{2.8e18}{\centi\meter^{-3}}$')
# ax.plot(ll, f(ll, *params1), '-', color='r', label=r'Fit $f(\lambda^2) = \alpha_1\lambda^2 + \beta_1$, $N=\SI{1.2e18}{\centi\meter^{-3}}$')
# ax.plot(ll, f(ll, *params2), '-', color='#2c5194', label=r'Fit $f(\lambda^2) = \alpha_2\lambda^2 + \beta_2$, $N=\SI{2.8e18}{\centi\meter^{-3}}$')
# ax.set_xlabel(r'$\lambda^2 \:/\: \si{\micro\meter}$')
# ax.set_ylabel(r'$\frac{\Theta}{d} \:/\: \si{\radian\meter^{-1}}$')
# leg1 = ax.legend(loc='best', fancybox=False, fontsize='small', edgecolor='k')
# leg1.get_frame().set_linewidth(0.3)
#
# # Einstellung der Achsen
# ax.set_xlim(0.8, 7.2)
# ax.set_ylim(40, 200)
# ax.xaxis.set_minor_locator(AutoMinorLocator())
# ax.yaxis.set_minor_locator(AutoMinorLocator())
# ax.tick_params(axis='both', direction='in')
# ax.tick_params(which='major', direction='in', length=7, width=0.3)
# ax.tick_params(which='minor', direction='in', length=4, width=0.3)
#
# # in matplotlibrc leider (noch) nicht möglich
# plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
# plt.savefig('plots/GaAs2.pdf')
#
#
# ################################################################################
# Weitere Berchnungen

# Maximales B-Feld
a = paramsB[0]
b = paramsB[1]
c = paramsB[2]
d = paramsB[3]

zmax = 1/(12*2**(1/3)*a) * ((np.sqrt((-432*a**2*d + 216*a*b*c - 54*b**3)**2 + 4*(24*a*c-9*b**2)**3) - 432*a**2*d + 216*a*b*c - 54*b**3)**(1/3)) - (24*a*c - 9*b**2)/(6*2**(2/3)*a* (np.sqrt((-432*a**2*d + 216*a*b*c - 54*b**3)**2 + 4*(24*a*c-9*b**2)**3) - 432*a**2*d + 216*a*b*c - 54*b**3)**(1/3)) - b/(4*a)

Bmax = Bfit(zmax, *paramsB)

print('\n\nMaximales B-Feld')
print('z_max = ', zmax, 'mm')
print('B_max = ', Bmax, 'mT')


# # Effektive Masse
# print('\n\nBerechnung der effektiven Masse:')
# e0 = con.e
# eps = con.epsilon_0
# c = con.c
# n = 3.3543
# N1 = 1.2e18#*10**(-6)
# N2 = 2.8e18#*10**(-6)
# Bmax = Bmax*10**(-3) # T
#
# a1 = ufloat(params1[0], err1[0])*10**6
# a2 = ufloat(params2[0], err2[0])*10**6
#
# def m(a, N):
#     return unp.sqrt((e0**3)/(8*np.pi**2*eps*c**3) * (N*Bmax)/n * 1/a)
#
# # def m2(a, N):
# #     return unp.sqrt(a*N*Bmax/(n*a))*con.m_e
#
# mtheo = 0.067 # m_e
# m1 = m(a1, N1)/con.m_e # m_e; N = 1.2e18
# m2 = m(a2, N2)/con.m_e # m_e; N = 2.8e18
#
# print('GaAs, N = 1.2e18: m* = ', m1)
# print('GaAs, N = 2.8e18: m* = ', m2)
# print('Theorie: ', mtheo)
#
# ################################################################################
# # Diskussion
#
# def Abw(exp, theo):
#     return (exp - theo)/theo
#
# print('\n\nAbweichungen zum Theoriewert')
# print('Delta m* (N = 1.2e18) = ', Abw(m1, mtheo))
# print('Delta m* (N = 2.8e18) = ', Abw(m2, mtheo))
