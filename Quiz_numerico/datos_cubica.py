import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

datos = pd.read_table('datos_cubica.txt', delimiter=' ')
dist = np.array(datos['Distancia'].values)
vel = np.array((datos['Velocidad'].values))

ajuste = np.polyfit(dist, vel, 3)
a,b,c,d = ajuste[0], ajuste[1], ajuste[2], ajuste[3]
print(ajuste)
ecuacion = a*(dist**3)+b*dist**2+c*dist+d
etiqueta_eq = 'y='+str(a)+'y+'+str(b)+'$y^{3}$'

plt.figure()
plt.plot(dist,vel, marker='.', color='k', ls='', label='Datos experimentales')
plt.plot(dist, ecuacion, color='r', ls='-', label='')
plt.legend()
plt.grid(ls='--')
plt.show()
plt.close()