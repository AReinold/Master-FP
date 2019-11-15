import matplotlib.pyplot as plt
import numpy as np
import math
import cmath as cm
plt.rcParams['text.usetex'] = True
plt.rcParams['text.latex.unicode'] = True
plt.rcParams['text.latex.preamble'] = [r'\usepackage{amsmath}']
plt.rcParams['text.latex.preamble'] = [r'\usepackage{siunitx}']
#Geometriewinkel
g1=0.5572*math.pi/180
g2=0.5862*math.pi/180
g=(g1+g2)/2
#Reflekscan:
winkel1, counts1 = np.genfromtxt('reflekscan1.uxd', unpack = True)
#Diffscan
winkel2, counts2 = np.genfromtxt('diffscan1.uxd', unpack = True)
winkel1= winkel1*math.pi/180

#Bereinigung
winkel3, counts3 = winkel1, counts1-counts2
print(1)
#print(counts3)
fig1, ax1 = plt.subplots()
#fig2, ax2 = plt.subplots()
#fig3, ax3 = plt.subplots()
ax1.plot(winkel3, counts1,'r',label='Messwerte')
ax1.plot(winkel3, counts3,'g',label='Korrigierte Messwerte')
ax1.plot(winkel3, counts2,'b',label='Diffuser Scan')
ax1.set_yscale('log')
ax1.set_ylabel('Intensität',fontsize = 12)
ax1.set_xlabel(r'Wellenvektorübertrag $\vec{q}_z\,[\frac{1}{\si{\angstrom}}]$',fontsize = 12)
ax1.legend()
#ax2.set_yscale('log')
#ax3.set_yscale('log')

#plt.plot(winkel3, np.log(counts3),'g')
#plt.plot(winkel1, np.log(counts1), 'b')
#plt.plot(winkel2, np.log(counts2), 'r')

#plt.plot(winkel3, counts3,'g')
#plt.plot(winkel1, counts1, 'b')
#plt.plot(winkel2, counts2, 'r')

#Geometriefaktor
D=0.02

for i in range(501):
    G=D*np.sin(winkel1[i])/0.0002
    if(winkel1[i]>0):
        if(winkel1[i]<g):
            counts3[i]=counts3[i]/(G)

#plt.show()
########################################################################
n1=1; #Luft
n2=1-1.2e-6; #Schicht #<-Amplituden
n3=1-7.4e-6; #Substrat#<- Amplituden
c=cm.sqrt(-1)
#Rauigkeit
sigma1=15.5e-10; #Schicht

sigma2=9.8e-10; #Substrat
#############################################################
#Schichtdicke
z2=873e-10;         #<- Ändert Periodendauer
#Einfallswinkel
counts3=counts3/counts3[39]  #1117270      #7570340.1

a_i=np.array([])
for j in range(0,501):
    b=np.array([0.005*j*math.pi/180+0*c])
    a_i=np.append(a_i,b)
#Wellenvektorübertrag
#print(a_i)
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
fig4, ax4 = plt.subplots()
qz_1=4*math.pi/1.54*np.sin(winkel3)
ax4.plot(qz,x1_1,label = r'Theoriekurve',color='r')
ax4.plot(qz_1,counts3,label = 'Messwerte',alpha=0.35,marker='x',color='b')
ax4.set_yscale('log')
plt.xlim(0.012,0.25)
plt.ylim(10**-6,10**1)
plt.legend()
ax4.set_ylabel('Intensität',fontsize = 12)
ax4.set_xlabel(r'Wellenvektorübertrag $\vec{q}_z\,[\frac{1}{\si{\angstrom}}]$',fontsize = 12)
#xlabel('q_z [A^{-1}]');
#ylabel('intensity');
#data = csvread('diffscan2.txt');
#plot (data (:,1), data (:,2));
#set au
plt.show()
#replot
