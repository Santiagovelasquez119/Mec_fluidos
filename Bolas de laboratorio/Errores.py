import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import t

datos = pd.read_table("radios.txt")
info = np.array(datos['Datos'].values)
media = info.mean()

# Importación del archivo
datos_2 = pd.read_table("Longs.txt", delimiter=' ')

# Definición de variables
# Obtenemos los valores de la columna promedio y se convierte en un array de python
temp_prom = np.array(datos_2['Promedio'].values)
# Se obtienen los datos de la columna longs y se convierte en array de python
longs = np.array(datos_2['longs'].values)
# Tomamos todos los tiempos reportados de todas las filas(:) y de la columna uno a la once(1:11)
tiempos = np.array(datos_2)[:, 1:-2]
# Hacemos la transpuesta de los tiempos para poder plotear la gráfica
tiempos = np.transpose(tiempos)

# se realiza el ajuste de los datos a una gráfica de grado 1: y=ax+b
coef = np.polyfit(temp_prom, longs, 1)
# Definimos las variables a y b como los coeficientes de la ecuación
a, b = np.round(coef[0], 3), np.round(coef[1], 3)

ecuacion = a*temp_prom+b
marca = 'y= '+str(a)+'x +'+str(b)

# Se crea un nuevo gráfico y se añade un títuo
plt.figure()
plt.title('Datos guía')
# Se plotean todos los tiempos para los datos de longitud y se añade una etiqueta con el número del experimento
for i in range(tiempos.shape[0]):
    x = tiempos[i]
    plt.plot(x, longs, '.', label='Exp'+str(i+1))

# Se definen los nombres de los ejes
plt.xlabel('Tiempo promedio (s)')
plt.ylabel('Longitud (cm)')
# Se añade la cuadrícula
plt.grid(ls='--')
# plt. legend sirve para visualizar las etiquetas
plt.legend(loc='best')
# plt.savefig('Datos experimento bolas esfera.pdf', dpi=150)
# plt.show()
plt.close()

plt.figure()
plt.title('Datos guía y ajuste')
for i in range(tiempos.shape[0]):
    x = tiempos[i]
    plt.plot(x, longs, '.', color='k')
plt.plot(temp_prom, longs, marker='.', color='k', ls='', label='Datos experimentales')
plt.plot(temp_prom, ecuacion, color='r', ls='--', label=marca)
plt.xlabel('Tiempo (s)')
plt.ylabel('Longitud(cm)')
plt.grid(ls='--')
plt.legend()
plt.savefig('Ajuste experimento bolas.pdf', dpi=150)
#plt.show()
plt.close()
# ----------------------Propagación de errores------------------------
# Error sistemático: Error ligado al equipo de medición
# Error aleatorio: Ligados a un componente estadístico

const_grav = float(input('Ingrese la constante gravitacional en m/$s^{2}$: '))
dens_c = float(input('Ingrese la densidad de la canica en kg/$m^{3}$: '))
dens_f = float(input('Ingrese la densidad del fluído en kg/$m^{3}$: '))
er_lon=float(input('Ingrese el error en la longitud: '))
er_tiem = float(input('Ingrese el error en el tiempo: '))
er_grav = float(input('Ingrese el error en la gravedad: '))
er_rad = float(input('Ingrese el error en los radios: '))
er_dens_c = float(input('Ingrese el error en la densidad de la canica: '))
er_dens_f = float(input('Ingrese el error en la densidad del fluído: '))

#---------------Definición de variables---------------------
er_relat_lon = er_lon/np.min(longs)
er_relt_tem = er_tiem/np.min(temp_prom)
er_relat_grav = er_grav/const_grav
er_relat_rad = er_rad/media
er_relat_difmean = np.sqrt((er_dens_c**2+er_dens_f**2))/(dens_c-dens_f)
tam_muest_rad = info.shape[0]
tam_muest_tiem = tiempos.shape[1]
visc = (2/9)*(dens_c-dens_f)*(const_grav)*(media**2)*(1/(a))*0.01

#-------------Parámetro t-student para los radios------------
t_1 = t.interval(0.95, tam_muest_rad-1)[1]
t_1 = np.round(t_1,3)
stand_desv_rad = np.sqrt((1/(tam_muest_rad-1))*(sum((info-media)**2)))
error_aleatorio_rad = (t_1*stand_desv_rad)/(np.sqrt(tam_muest_rad))
stand_desv_vel = np.sqrt((np.sum((longs-b-a*temp_prom)**2))/(tiempos.shape[1]-2))
er_sist_vel = np.sqrt(er_relat_lon**2 + er_relt_tem**2)
sxx = np.sum((temp_prom - np.mean(tiempos))**2)
t_2 = round(t.interval(0.95, 5-2)[1], 3)
er_aleat_vel = (1/a)*t_2*(stand_desv_vel/np.sqrt(sxx))
er_visc = np.sqrt((er_relat_difmean)**2+(er_grav)**2+(2*(er_relat_rad**2))+er_sist_vel**2)
# ------------------------------------------------------------------
print('\n')
print('+--------------------------Datos experimentales---------------------------+')
print(f'y=ax+b --> a={a} y b={b}\nVelocidad límite= {a}\nViscosidad= {visc}')

print('+-----------------Propagación de errores relativos-----------------------+')
print(f"El error relativo en la longitud es= {np.round(er_relat_lon,5)}")
print(f'El error relativo en el tiempo es= {np.round(er_relt_tem,5)}')
print(f'El error relativo en la gravedad es= {round(er_relat_grav,5)}')
print(f'El error relativo en el radio es= {round(er_relat_rad,5)}')
print(f'El error relativo aleatorio en el radio es= {round(error_aleatorio_rad,5)}')
print(f'El error relativo total en el radio es= {round(error_aleatorio_rad+er_relat_rad,5)}')
print(f'El error relativo en la diferencia de las densidades es= {round(er_relat_difmean,5)}')
print(f'El error sistemático en la velocidad límite es= {round(er_sist_vel,5)}')
print(f'El error aleatorio en la velocidad límite es= {round(er_aleat_vel,5)}')
print(f'El error sistemático total de la velocidad límite es= {round(np.sqrt(er_sist_vel**2+er_aleat_vel**2),5)}')
print(f'El error en la viscosidad es={er_visc}')
print('+-------------------------------------------------------+')



