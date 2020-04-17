# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 10:37:22 2020

@author: Cecilia
"""
import numpy as np
import matplotlib.pyplot as plt

#Defino campo vector
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

#%%Derivada del campo vector
def der_campo_vector(x):
# Calculamos dx
    dx = x[1]-x[0]
    # Aproximamos la derivada como df/dx
    df = np.diff(campo_vector(x))/dx
    return df
df = der_campo_vector(x)
plt.figure(2)
plt.plot(der_campo_vector(x))
plt.show
#%% Inestabilidad o estabilidad en puntos fijos
for i in x0:
    # i es el valor de x, buscamos que indice del array le corresponde
    # Una forma de buscarlo es la siguiente:
    indice = np.argmin(np.abs(i-x))
    # Primero hacemos la diferencia entre el punto fijo que estamos/
    # mirando y todos los puntos del array
    # Despues hacemos valor absoluto de esto
    # Y con np.argmin nos da el indice donde esta el minimo de esto/
    # (o sea el indice del punto del vector mas cercano al punto fijo)
    print(indice)
    print(x[indice])
    # Ahora miramos el vector de derivadas en ese mismo punto:
    if df[indice] > 0:
        print(df[indice])
        print('es inestable')
    elif df[indice] < 0:
        print(df[indice])
        print('es estable')
