# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 10:37:22 2020

@author: Cecilia
"""
import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(-1.5, 1.5, 1000)

def campo_vector(x):
    f = x-x**3
    return f
plt.figure(1)
plt.plot (campo_vector(x))

plt.show
#%% Busco Raíces
x0 = np.roots([-1,0,1,0])
print (x0)
#%% Quiero automatizar el cálculo de la derivada pero
#   después al momento de querer ver la estabilidad
#   de puntos fijos me tira error :(
#   *Creo* que ocurre algo raro con el dominio de la función
#   al hacer np.diff
def der_campo_vector(x):
    df = np.diff(campo_vector(x))
    return df
plt.figure(2)
plt.plot(der_campo_vector(x))
plt.show
#%% Inestabilidad o estabilidad en puntos fijos

for i in x0:
    if der_campo_vector(i) > 0:
        print(der_campo_vector(i))
        print('es inestable')
    elif der_campo_vector(i) < 0:
        print(der_campo_vector(i))
        print('es estable')
