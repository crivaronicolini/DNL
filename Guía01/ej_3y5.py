# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 22:39:30 2020

@author: Cecilia
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import scipy.optimize as opt

#Ejercicio 3

a = 0.06 #tasa de crecimiento del tumor
b = 0.25 #tamaño final y estable al que crece el tumor
N0 = 0.01
t = np.linspace(0,150,1000)

def N_punto(N, t):
    dN = -a*N*np.log(b*N)
    return dN
N = odeint(N_punto, N0, t)

dN = N_punto(N, t)

plt.figure(1)
plt.plot (t, N, label = 'N(t)')

plt.figure(2)
plt.plot (N, dN, label = 'campo vector')

plt.show


#%% Ejercicio 5
#No me sale buscar raíces 
raíz = opt.fsolve(N_punto , N, t)
print(raíz)
#%%
# Derivada segunda
def der_N_punto(N):
# Calculamos dn
    dn = N[1]-N[0]
    # Aproximamos la derivada como df/dt
    dN_2 = np.diff(dN)/dn
    return dN_2
dN_2 = der_N_punto(N)
plt.figure(3)
plt.plot(dN_2)
plt.show
#%%
# Inestabilidad o estabilidad en puntos fijos, cuando tenga las raíces /
# hago esta parte

