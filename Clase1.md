# Miércoles 15/04, Teoría:
Bibliografía: Libro de Gabo, nos va a pasar los capítulos en Word.
Recomienda el Strogatz (descargado de estufis)
Guckenhemer, buen libro pero pesado y "poco juvenil" en el tema.
Wiggins, estudiante de Guckenhemer, escribió un libro más largo y claro.
Arrowsmith, sirve para el final de la carrera.
Dynamical systems with aplications using Python, Lynch.

*Repaso de Newton:

-Tasas de la variación de las variables en función del tiempo, lo que permite entender ecuaciones no elípticas.

-Describir a partir de unas odes un sistema dinámico.

-Problema de dos cuerpos, interacción entre ellos, fuerza gravitatoria, no lineal. Resolución: pararse en CM, usar masa reducida, usar conservación de momento angular. Al hacer la parte radial y la angular quedan ecs no lineales. La que describe la parte radial, si defino  u=1/r y la fuerza va como 1/r^2, obtengo la ecs del oscilador armónico, ahora tengo un problema lineal. Resuelvo este problema y vuelvo a las variables originales y llego a la ec de las elipses.
Esto, ¿Es posible en general? No, pero en el proceso de intentar hacerlo algorítmicamente vamos a poder simplificar términos y parámetros, esto lo vamos a ver a lo largo del curso.
Si hacemos el problema de tres cuerpos, no nos da analíticamente. Poincaré dijo que el problema no es la resolución analítica sino la perspectiva y la geometría.

*Vocabulario:
Nos centramos en ODE's, pero si tengo derivadas parciales de un campo, puedo escribir dicho campo como suma de elementos de una base. El tema en general es que se tiene infinitas ecuaciones, pero dado que hay términos disipativos, un conjunto finito de ecuaciones son las que están activas. Esto también lo vamos a ver a lo largo del curso.

Si por ejemplo tengo la ecuación del oscilador armónico con término disipativo, puedo definir dxdt=v y por lo tanto dvdt=1/m(-beta.v - kx) y podemos hacer un campo vector. Si el campo vector es una función lineal de las variables decimos que el sistema es lineal. Caso contrario, el sistema es no lineal. (Caso no lineal, péndulo físico). Un conjunto de ODE's con campo vector suficiente suave da solución única. El espacio de fases es el espacio en el cual yo sé que un punto tiene solución única. En el caso del péndulo, tengo trayectorias cerradas (pequeñas oscilaciones), situación crítica (de -pi a pi) y trayectorias grandes que no son cerradas en el espacio de fase. También se tiene el caso de que haya término forzado, una fuerza externa donde aparece explícitamente el tiempo.

# Ejemplo de péndulo, caso simple, de órbita cerrada, después hago para los otros casos:
'''
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
th0 = 0
dxth0= 15
x0 = th0, dxth0
t = np.linspace(0, 20, 1000)
g = 10
l = 0.1

def model(y, t):
    x, v = y
    dxdt = v
    dvdt = -g/l*np.sin(x)
    return dxdt, dvdt

x, v = odeint(model, x0, t).T

plt.plot(x,v)
#plt.plot(t,x,label='theeta')
#plt.plot(t,v,label='theeta_punto')
plt.xlabel('theeta')
plt.ylabel('theeta_punto')
plt.legend()

plt.show
'''


Sistema lineales: dxdt = ax
Muestra la diferencia entre gráficos de x vs t y el espacio de fases de x.
Por ejemplo, crecimiento en población.

Sistemas no lineales: dxdt=ax(1-x/N) para x grande esta derivada se vuelve negativa.

El capítulo del libro de Gabo muestra este ejemplo, lo resuelve analíticamente integrando y muestra el espacio de fases. Lo más importante de esto es ver que hay multiplicidad coexistente de estados estacionarios en dicho espacio, eso determina la dinámica de estabilidad de estos sistemas.

¿Es posible aproximar a las soluciones de un problema no lineal por aquellas del problema linealizado? Sí (el libro de Gabo lo explica con detalle). Por ejemplo en caso del péndulo, aproximar sen(theeta) por theeta para pequeñas oscilaciones. Esta pregunta igual tiene su trampa, el problema no lineal debe cumplir ciertas condiciones. Está mostrando cómo se resuelve haciendo Taylor, mostrando cómo se comporta la derivada en ciertos puntos.

¿Cómo afectan nuestros parámetros al sistema? Dió el ejemplo de péndulo sobreamortiguado. Pregunta super importante para la materia.
