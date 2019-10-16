import numpy as np
import matplotlib.pyplot as plt
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy.optimize import curve_fit
import scipy.constants as const

R=1
N=154
I1=0.044
I2=0.069
I3=0.095
I4=0.120
I5=0.330
I6=0.372
I7=0.447
I8=0.522
I9=0.600
I10=0.537


B=const.mu_0*((8*I10*N)/(np.sqrt(125)*R))

print(B)
