import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

datos = pd.read_table('datos.txt', delimiter=' ')
X = np.array(datos['X'].values)
Y = np.array(datos['Y'].values)

ajuste = np.polyfit(X,Y,1)
m,b = np.round(ajuste[0],4), np.round(ajuste[1],4)
ecuacion = m*X+b
etiqueta= 'y='+str(m)+'x+'+str(b)

plt.figure()
plt.plot(X,Y, marker='.', ls='', color='k', label='Datos experimentales')
plt.plot(X,ecuacion, ls='--',color='r',label=etiqueta)
plt.grid('--')
plt.xlabel('Instrumento patrón')
plt.ylabel('Instrumento prueba')
plt.legend()
#plt.show()
plt.close()

valor = m*(3.8)+b
#print('El valor para x=3.8 es:', valor)

#----------------------Ejercicio #2-------------------------


#----------------------Ejercicio #3-------------------------
diametro = 6
presion_atm = 1.97385
R_c = 0.08206
T = 20+273.15
volumen = ((4/3)*np.pi*(diametro/2)**3)*1000
#print('El volumen es:', volumen,'L')

moles = round((presion_atm*volumen)/(R_c*T),4)
kilomol = moles*0.001
#print('El numero de moles presentes es:',moles)
#print('El numero de kilomoles es:',kilomol)
peso_Kg = round((moles*4.0026)/1000,4)
#print('El peso en Kg del Helio en la esfera es:',peso_Kg)