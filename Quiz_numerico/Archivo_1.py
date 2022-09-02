import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Importación del archivo
datos = pd.read_table('datos.txt', delimiter=' ')

temp = np.array(datos['Temperatura'].values)
visc = np.array(datos['Viscosidad'].values)

X = 1/temp
Y = np.log(visc)

ajuste = np.polyfit(X,Y,1)
a,b = np.round(ajuste[0],2), np.round(ajuste[1],2)
ecuacion = a*X+b
etiqueta = 'y='+str(a)+'x'+str(b)

plt.figure()
plt.plot(X, Y, marker='.', color='k', ls='')
plt.plot(X, ecuacion, color='r',ls='--', label=etiqueta)
plt.grid('--')
plt.legend()
plt.show()
plt.close()


