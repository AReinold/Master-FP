import matplotlib.pyplot as plt
import numpy as np
import math
import cmath as cm
plt.rcParams['text.usetex'] = True
plt.rcParams['text.latex.unicode'] = True
plt.rcParams['text.latex.preamble'] = [r'\usepackage{amsmath}']
plt.rcParams['text.latex.preamble'] = [r'\usepackage{siunitx}']
c=cm.sqrt(-1)
#Geometriewinkel
g1=0.5572*math.pi/180
g2=0.5862*math.pi/180
g=(g1+g2)/2
#Reflekscan:
winkel1, counts1 = np.genfromtxt('reflekscan1.uxd', unpack = True)
#Diffscan
winkel2, counts2 = np.genfromtxt('diffscan1.uxd', unpack = True)
#norm=counts1[2]
#counts1=counts1/norm
#counts2=counts2/norm
#Konvertierung auf rad:
winkel1= winkel1*math.pi/180
#Probendurchmesser:
D=0.01046
print('g:')
print(g)
#Geometriefaktorkorrektur
#Bereinigung
print('NOOT:')
print(counts1[0])
#Konvertierung auf Wellenvektorübertrag
winkel3, counts3 = winkel1, counts1-counts2
qz_1=4*math.pi/1.54*np.sin(winkel3)
#Erster Plot
print(counts2[0])
for i in range(501):
    G=D*np.sin(winkel1[i])/0.0001047#<-Höhe des Strahls
    if(winkel1[i]>0):
        if(winkel1[i]<g):
            counts1[i]=counts1[i]/(G)
            counts2[i]=counts2[i]/(G)
norm=counts1[1]
counts1=counts1/norm
counts2=counts2/norm
counts3 = counts1-counts2
fig1, ax1 = plt.subplots()
ax1.plot(qz_1[1:500], counts1[1:500],'r',label='Messwerte')
ax1.plot(qz_1[1:500], counts3[1:500],'g',label='Korrigierte Messwerte')
ax1.plot(qz_1[1:500], counts2[1:500],'b',label='Diffuser Scan')
ax1.set_yscale('log')
ax1.set_ylabel('Intensität',fontsize = 12)
ax1.set_xlabel(r'Wellenvektorübertrag $\vec{q}_z\,[\frac{1}{\si{\angstrom}}]$',fontsize = 12)
ax1.legend()
plt.xlim(0,0.35)
winkel3, counts3 = winkel1, counts1-counts2
#janky "Normierung"
norm2=counts3[25]
counts3=counts3/norm2
print(counts3[0])  #1117270      #7570340.1
#Parrat-Algo
########################################################################
n1=1; #Luft
n2=1-1e-6; #Schicht #<-Amplituden
n3=1-6.9e-6; #Substrat#<- kritischer Winkel
#Rauigkeit
sigma1=15.5e-10; #Schicht

sigma2=9.8e-10; #Substrat
#Schichtdicke
z2=873e-10;         #<- Ändert Periodendauer
#############################################################
#Einfallswinkel
a_i=np.array([])
for j in range(0,501):
    b=np.array([0.005*j*math.pi/180+0*c])
    a_i=np.append(a_i,b)
#Wellenvektorübertrag(für das Skript)
qz=4*math.pi/1.54*np.sin(a_i);
#Betrag des Wellenvektors
k=2*math.pi/1.54*1e10;
#z-Komponenten
kz1=k*np.sqrt(n1**2-np.cos(a_i)**2);
kz2=k*np.sqrt(n2**2-np.cos(a_i)**2);
kz3=k*np.sqrt(n3**2-np.cos(a_i)**2);
#modifizierte Fresnelkoeffizienten
r12=(kz1-kz2)/(kz1+kz2)*np.exp(-2*kz1*kz2*sigma1**2);
r23=(kz2-kz3)/(kz2+kz3)*np.exp(-2*kz2*kz3*sigma2**2);
x2=np.exp(-2*c*kz2*z2)*r23;
x1=(r12+x2)/(1+r12*x2);
x1_1=np.abs(x1)**2
#zweiter Plot
fig4, ax4 = plt.subplots()
ax4.plot(qz,x1_1,label = r'Theoriekurve',color='r')
ax4.plot(qz_1,counts3,label = 'Messwerte',alpha=0.35,color='b')
ax4.set_yscale('log')
plt.xlim(0.012,0.25)
plt.ylim(10**-6,10**1)
plt.legend()
ax4.set_ylabel('Intensität',fontsize = 12)
ax4.set_xlabel(r'Wellenvektorübertrag $\vec{q}_z\,[\frac{1}{\si{\angstrom}}]$',fontsize = 12)
plt.show()
