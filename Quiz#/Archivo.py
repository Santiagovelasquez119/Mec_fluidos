import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import t

#importación del archivo
datos = pd.read_table('datos.txt', delimiter=' ')

#Definición de variables
longitudes = np.array(datos['Longitud'].values)
tiempo = np.array(datos['tiempo'].values)

#Errores
er_long = 0.0001
er_time = 0.23
er_grav = 0.1
er_esf = 0.000001
er_dens = 0.001
#datos del ejercicio
dens_c = 17.853
dens_f = 17.840
grav = 32.2
rad_esf = 0.000621

#Gráfica y ajuste
ajuste = np.polyfit(tiempo, longitudes, 1)
a,b = np.round(ajuste[0],4), np.round(ajuste[1],4)
ecuacion = a*tiempo+b
etiqueta = 'y='+str(a)+'x''+'+str(b)

plt.figure()
plt.title('Datos experimentales')
plt.plot(tiempo, longitudes, ls='', marker='.', color='k', label='Datos experimentales')
plt.xlabel('Tiempo(s)')
plt.ylabel('Longitud(pie)')
plt.grid(ls='--')
plt.plot(tiempo, ecuacion, ls='--', color='r', label=etiqueta)
plt.legend()
plt.savefig('Datos experimentales Quiz#1', dpi=150)
#plt.show()
plt.close()

#definición de variables
er_sist_long = er_long/min(longitudes)
er_sis_time = er_time/min(tiempo)
er_sist_grav = er_grav/grav
er_sist_esf = er_esf/rad_esf
er_sist_difmean = np.sqrt(er_dens**2+er_dens**2)/(dens_c-dens_f)
vel_prom = a
er_sist_vel = np.sqrt(er_sist_long**2 + er_sis_time**2)

stand_desv_vel = np.sqrt((np.sum((longitudes-b-a*tiempo)**2))/(5-2))
sxx = np.sum((tiempo - np.mean(tiempo))**2)
t_2 = round(t.interval(0.95, 5-2)[1], 3)
er_aleat_vel = (1/a)*t_2*(stand_desv_vel/np.sqrt(sxx))

print('El error sistemático en la longitud es:',round(er_sist_long,4))
print('El error sistemático en el tiempo es: ', round(er_sis_time,4))
print('El error sistemático en la gravedad es:', round(er_sist_grav,4))
print('El error sistemático en la esfera es', round(er_sist_esf,4))
print('El error en la diferencia de las densidades es: ', round(er_sist_difmean,4))
print('La velocidad promedio es: ',a)
print('El error sistemático en la velocidad límite es:',round(er_sist_vel,4))
print('El error aleatorio en la velocidad límite es:',round(er_aleat_vel,4))













