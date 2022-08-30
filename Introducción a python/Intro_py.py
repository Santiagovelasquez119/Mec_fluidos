import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
#Se realiza la importación de las librerías; lo que está luego del as es una simplificación para no escribir
#todo el nombre Literalmente dice importar numpy como np, entonces para llamarla se hace uso del apodo

datos = pd.read_csv('Datos_poly3.csv', delimiter=';')
#Se hace la lectura del archivo entregado, es necesario especificar la ruta si el archivo .py no se encuentra en la misma
#carpeta que el archivo

x = datos['x'].values
y = datos['y'].values
#Una vez cargados los archivos se almacen las columnas 'x' y 'y' en las variables x, y

plt.figure()
#Crea una nueva figura
plt.plot(x,y, marker = 'o', color = 'k', ls = '')
#Añade a la figura los valores de x, y guardados anterior mente
#ls se refiere a la unión de los puntos, luego si está vacío solo mostrará los puntos sin unión

plt.xlabel('datos x')
#Agrega una etiqueta en el eje x con el nombre que le asignamos, en este caso datos x
plt.ylabel('datos y')
#Agrega una etiqueta en el eje y con el nombre que le asignamos, en este caso datos y

#plt.show()
plt.close()

coef = np.polyfit(x, y, 3)
a = np.round(coef[0],3)
b = np.round(coef[1],3)
c = np.round(coef[2],3)
d = np.round(coef[3], 3)
#Realiza el ajuste con la librería np y se guardan los coeficientes en las variables a,b,c,d
##ax3+bx2+cd+d

ecuacion = a*(x**3)+b*(x**2)+c*(x)+d
etiqueta ='y =' + str(a) + '$x^{3}$ +' + str(b)+'$x^{2}$ +' + str(c) + '$x$ + ' + str(d)

plt.figure()

plt.plot(x,y, marker = 'o', color = 'k', ls = '')
plt.plot(x,ecuacion, color = 'r', ls = '-',label= etiqueta)


plt.xlabel('datos x')
plt.ylabel('datos y')
plt.legend()
#plt.show()
#plt.close()

plt.savefig('Mi_primer_ajuste.png', dpi=150)
#dpi se refiere a la resolución de la imagen













