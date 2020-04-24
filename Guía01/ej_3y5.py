# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 22:39:30 2020

@author: Cecilia
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import scipy.optimize as opt

# Ejercicio 3

a = 0.06  # tasa de crecimiento del tumor
b = 0.25  # tamaño final y estable al que crece el tumor
N0 = 0.01
t = np.linspace(0, 150, 1000)


def N_punto(N, t):
    dN = -a*N*np.log(b*N)
    return dN


N = odeint(N_punto, N0, t).reshape(np.shape(t))

dN = N_punto(N, t)

plt.subplot(1, 3, 1)
plt.plot(t, N, label='N(t)')
plt.title('Trayectoria')
plt.xlabel('Tiempo')
plt.ylabel('N')

plt.subplot(1, 3, 2)
plt.plot(N, dN, label='campo vector')
plt.title('campo vector')
plt.xlabel('N')
plt.ylabel('Ṅ')


# %% Ejercicio 5
# fsolve te pide un valor estimativo para buscar la raíz, le pido que /
# busque cerca de N=3 y t=100 (a partir de los gráficos me doy una idea)
raices = opt.fsolve(N_punto, 3, 100)
# %% Acá es donde tengo el ValueError
# Derivada segunda


def der_N_punto(N):
    # se puede poner n=2 para diferenciar dos veces
    dN_2 = np.diff(N, n=2)
    return dN_2.ravel()


dN_2 = der_N_punto(N)
plt.subplot(1, 3, 3)
plt.plot(dN_2)
plt.title('Derivada segunda')
plt.xlabel('t')
plt.ylabel('Ñ')

plt.show()

# %% cuando la derivada segunda funque armo bien esto
# hago una mascara para encontrar bien la raiz, lo anterior
# no funciona porque dN_2 nunca es exactamente == 4.
epsilon = 0.1
print(f'raices={raices}')

for raiz in raices:
    print(f'raiz: {raiz}')
    mask = (t >= (raiz - epsilon)) & (t <= (raiz + epsilon))
    # le aplico esa mascara a t, que es el eje x de dN_2
    # y me devuelve el indice exacto que estoy buscando
    indice = np.where(mask)[0][0]
    valor = dN_2[indice]
    if valor > 0:
        print(f'{valor} -> es inestable')
    elif valor < 0:
        print(f'{valor} -> es estable')
