import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.optimize import curve_fit
from scipy.optimize import brentq
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy.stats import stats

DeltaLambdaRot = 48.94e-12
DeltaLambdaBlau = 27.95e-12

LambdaRot = 643.8e-9
LambdaBlau = 480e-9
hquer=6.62607004e-34
c0=299792458.0
gth1 = 1
gth2 = 1.75
gth3 = 0.5

B_Blau=1060e-3
muB = 9.274009994e-24

deltaLambdaBlau=0.5*83.29 / 100.8 * DeltaLambdaBlau

g_Blau = (hquer * c0 *deltaLambdaBlau)/(LambdaBlau**2 *muB *B_Blau)
print('delta lambda Blau: ',deltaLambdaBlau,'\ng_Blau: ',g_Blau)
