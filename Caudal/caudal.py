import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt

d=[[1,83.5,(30/36.6)],
   [2,76,(30/45.5)],
   [3,68,(30/60)],
   [4,59,(30/88.2)],
   [5,47,(30/160.1)],
   [6,34.5,(30/340.1)]]
datos = pd.DataFrame(d, columns = ['Dato','H (mm)','Q (LPS)'])
#print(datos)
datos.keys()

V=[30.0,30.0,30.0,30.0,30.0,30.0]

Y=datos['Q (LPS)']*1000  #paso a cm^3
X=datos['H (mm)']/10   #paso a cm
X=X**(5/2)

#Ajuste de la recta
XY=X*Y
X2=X**2
A=np.sum(XY)/np.sum(X2)
A=np.round(A,5)
AX=A*X
#print(A)

leyenda=u"Función Ajustada: Y =" + str (round(A,5)) + "X"
print(leyenda)

#plt.figure(figsize=(8,5))
#plt.plot(X,Y,"ro", label = "Datos experimentales")
#plt.plot(X,AX,color="b", ls="--", label = leyenda)
#plt.xlabel(u"H^(5/2)-[(cm)^(5/2)]", fontsize=14)
#plt.ylabel(u"Q-[(cm^3/s)]", fontsize=14)
#plt.grid(ls=":")
#plt.savefig("GRAFICA AJUSTE1.png",dp1=300) #guardar en carpeta
#plt.show()

angulo=15.1689 #agregar angulo
#tan_ang=np.tan(angulo*math.pi/180.)
#print(tan_ang)
tan_ang=24.4/(2*45)
g=978 # gravedad en cm/s^2
Cd= (15/8)*A/(tan_ang*np.sqrt(2*g))
Cd=np.round(Cd,5)
print ("Valor de Cd (coeficiente de descarga): ",Cd)

# Calculo de errores sistemáticos y aleatorios

#Error sistemático Volumen
dV_V=0.1/30
dV_V=np.round(dV_V,4)
print("Delta de V: ",dV_V)

#Error sistemático máximo en tiempo de aforo
dT_T=0.1/36.6
dT_T=np.round(dT_T,4)
print('Delta de T: ',dT_T)

#Error sistemático de los datos iniciales
dH_H=0.1/(datos["H (mm)"].min()) #se asume incertidumbre de 1mm/10mm
dH_H=np.round(dH_H,5)
print ("Delta de la altura: ",dH_H)

#dQ_Q=0.0001/(datos["Q (LPS)"].min()) #se asume incertidumbre de 0,1cm^3/1000cm^3
#dQ_Q=np.round(dQ_Q,5)
#print ("Delta del caudal: ",dQ_Q)

dQ_Q=np.sqrt(dV_V**2+dT_T**2) #Error sistematico, es indirecto
dQ_Q=np.round(dQ_Q,5)
print ("Delta del caudal: ",dQ_Q)

#Error sistematico de la pendiente
dA_As=np.sqrt((((5/2*dH_H)**2)+(dQ_Q)**2))
dA_As=np.round(dA_As,5)
print ("Error sistematico de la pendiente: ",dA_As)

#Error aleatorio en la pendiente
#Parámetro T-Student
from scipy.stats import t
N=len(Y)
t=t.interval(0.95,(N-1))[1]
#t=2.776445
t=np.round(t,3)

Y_AX= (Y-AX)**2
sd=np.sqrt(np.sum(Y_AX)/(N-1))
sd=np.round(sd,5)
print ("Valor de sd de la pendiente: ",sd)

dA_Aa=(1/A)*(t*sd)/(np.sqrt(np.sum(X**2)))
#print((np.sqrt(np.sum(X**2)))) #da diferente al del profee, a él le da 223,21748
dA_Aa=np.round(dA_Aa,5)
print ("Error aleatorio de la pendiente: ",dA_Aa) #diferente a la guía

#Agregar incertidumbre al ajuste, bandas de confianza
Ysup=AX+t*sd*np.sqrt(1+(X**2)/np.sum(X**2))
Yinf=AX-t*sd*np.sqrt(1+(X**2)/np.sum(X**2))

plt.figure(figsize=(8,5))
plt.plot(X,Y,"ro", label = "Datos experimentales")
plt.plot(X,AX,color="k", ls="--", label = leyenda)
plt.plot(X,Ysup,"b",lw=0.8)
plt.plot(X,Yinf,"g",lw=0.8)
plt.xlabel(u"H^(5/2)-[(cm)^(5/2)]", fontsize=14)
plt.ylabel(u"Q-[(cm^3/s)]", fontsize=14)
plt.grid(ls=":")
plt.legend(fontsize=14)
#plt.savefig("GRAFICA AJUSTE2.png",dp1=300) #guardar en carpeta
#plt.show()

#Error sistemático en el ángulo
#tomando una incertidumbre de 0.1°
inf_angulo=angulo-0.1
tan_inf=np.tan(inf_angulo*math.pi/180.)
print("Tangente de "+ str(inf_angulo)+": ",tan_inf)

sup_angulo=angulo+0.1
tan_sup=np.tan(sup_angulo*math.pi/180.)
print("Tangente de "+ str(sup_angulo)+": ",tan_sup)

incertidumbre=np.tan(0.1*math.pi/180.)
incertidumbre=np.round(incertidumbre,5)
print("tangente de 0.1: ", incertidumbre)

sistem_ang=incertidumbre/tan_inf
sistem_ang=np.round(sistem_ang,5)
print("error sistemático del angulo: ",sistem_ang)

#Error sistemático de la gravedad
g=978
sist_g=2/g  #se toma gravedad 978 +/- 1 cm/s^2
sist_g=np.round(sist_g,4)
print("error sistemático de la gravedad: ", sist_g)

#Error del coeficiente de descarga
ecd=np.sqrt(dA_As**2+dA_Aa**2+sistem_ang**2+(sist_g/2)**2)
ecd=np.round(ecd,5)
print("error coeficiente de descarga Cd: ",ecd) #por el aleatorio de la pendiente, da diferente a la guía

#reporte de resultados
print("reporte de Cd: ", Cd," +/- ",ecd*Cd) #redondear correctamente para un correcto reporte


#Si nos dan una profundidad H0=5,10 cm. ¿Cuál sería el caudal Q?
H0=5.20
Q0=Cd*(8/15)*tan_ang*np.sqrt(2*g)*(H0**2.5) #caudal en cm^3
print("Q0: ",Q0)

#Error sistemático del caudal
dH0_H0=0.1/H0  #incertidumbre de 1mm/10mm
dH0_H0=np.round(dH0_H0,5)
print("Error sistemático de Ho: ",dH0_H0)

ds_Q0=np.sqrt(ecd**2+sistem_ang**2+(sist_g/2)**2+((2.5*dH0_H0))**2)
ds_Q0=np.round(ds_Q0,5)
print("eeror sistemático de Q0: ",ds_Q0)

#Error aleatorio del caudal
da_Q0=1/Q0*t*sd*np.sqrt(1+(H0**5/np.sum(X**5)))
da_Q0=np.round(da_Q0,5)
print("Error aleatorio de Q0: ",da_Q0)

#Error total eN Q0
Q0_total=np.sqrt(ds_Q0**2+da_Q0**2)
Q0_total=np.round(Q0_total,5)
print("Error total de Q0: ",Q0_total )

#sesgo
sesgo=t*sd*np.sqrt(1+(H0**5/np.sum(X**5)))
sesgo=np.round(sesgo,5)

#Reporte del caudal Q0
print("reporte de caudal Q0: ",Q0," +/- ",sesgo ,"cm^3/s")  #tomar las cifras adecuadas para reporte correcto