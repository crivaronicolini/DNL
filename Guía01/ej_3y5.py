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
# fsolve te pide un valor estimativo para buscar la raíz, le pido que /
# busque cerca de N=3 y t=100 (a partir de los gráficos me doy una idea)
raíz = opt.fsolve(N_punto, 3, 100)
print(raíz)
#%% Acá es donde tengo el ValueError
# Derivada segunda
def der_N_punto(N):
# Calculamos dt
    dt = t[1]
    # Aproximamos la derivada como df/dt
    dN_2 = np.diff(dN, t)/dt
    return dN_2
dN_2 = der_N_punto(N)
plt.plot(dN_2)

#%% cuando la derivada segunda funque armo bien esto
if dN_2[raíz] > 0:
    print(dN_2[raíz])
    print('es inestable')
elif dN_2[raíz] < 0:
    print(dN_2[raíz])
    print('es estable')
