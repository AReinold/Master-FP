import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.optimize import curve_fit
from scipy.optimize import brentq
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy.stats import stats
#-------------------- a2--------------------------------------------------------
print('Phase:')
f, phase = np.genfromtxt('phase.txt', unpack=True)

plt.plot(f, phase, 'C2.', label='Messwerte')
plt.xscale('log')
plt.axvline(x=10000, ymin=0.0, ymax = 0.93, linewidth=1, color='C1')
plt.xlabel(r"$\nu\:/\:$Hz")
plt.ylabel(r"$\varphi\:/\:\circ$")
plt.legend(loc="best")
plt.tight_layout()
plt.savefig('phase.pdf')
plt.clf()
