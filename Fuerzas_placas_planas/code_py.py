import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches
import math

def a_triangulo(b,a):
    return b*a/2
def a_rectangulo(b,a):
    return(b*a)
def a_trapecio(a,b,h):
    t = h*(a+b)/2
    return t
def Ixc_triangulo(b,a):
    I=(b*(a**3))/36
    return I
def Ixyc_triangulo(b,a,d):
    I=(b*(a**2)/72)*(b-2*d)
    return I
def Ixc_rectangulo(b,a):
    I=(b(a**3))/12
    return I
def YC_trapecio(a,b,h):
    n=h*(a+2*b)
    d=3*(a+b)
    return n/d

points =np.array([30,10,5,15,10])

B1 = points[0]
b = points[1]
c = points[2]
H1 = points[3]
H2 = points[4]
B2 = b+2.*c
d = (B1-B2)/2

df = pd.DataFrame(columns=['Areas', 'Xc', 'Yc', 'XcA', 'YcA'], index=['A','B', 'Total'])

df['Areas']['A'] = a_trapecio(B1,B2,H1)
df['Areas']['B'] = a_triangulo(b,H2)

#Centroide del trapecio
df['Xc']['A'] = 0
df['Yc']['A'] = YC_trapecio(B1,B2,H1)

#Centroide del triangulo inferior
df['Xc']['B'] = 0
df['Yc']['B'] = H1+(b/3)

#Multiplicaciones d ela ecuacion
df['XcA'] = df['Areas']*df['Xc']
df['YcA'] = df['Areas']*df['Yc']

df['Areas']['Total'] = df['Areas'].sum()
df['XcA']['Total']=df['XcA'].sum()
df['YcA']['Total']= df['YcA'].sum()

#Centroide de la figura compuesta
YC = df['YcA']['Total']/df['Areas']['Total']

print(df)

#Distancia entre YC y los centroides de los triangulos laterales del trapecio
ytriang1 = YC-H1/3.

#Distancia entre YC y el cnetroide del rectangulo central del trapecio
yrect = YC-H1/2
print(yrect)

#Distancia entre YC y el centroide del triangulo superior
ytriang2 = (H1+H2/3)-YC

print('Distancias:', 'Triangulo_sup:',np.round(ytriang1))

#Base del triangulo
baseT = B1-B2

#Trapecio (Rectánglo y tri+angulo laterales)
iTrap = ((B2*H1**3)/12 + B2*H1*yrect**2) + (baseT*(H1**3)/36 + baseT*H1/2*ytriang1**2)

#Triangulo inferior
iTriang = b*(H2**3)/36 +b*H2/2*(ytriang2**2)

#Momentos de inercia del área compuesta (Ixx)
iComp = iTrap + iTriang
print(iComp)

print('Momentos de inercia respecto del centroide de la sección compuesta')
print(iTrap)
print(iTriang)
print(iComp)

##Centro de presion de la seccion compuesta respecto del borde izquierdo de la figura(repo  de acuerdo a la figura)
A = df['Areas']['Total']
XC = B1/2
XP = XC
YP = YC + iComp/YC/A #Centro de presión
print(YP)

#Para el ejemplo asumo la densidad del líquido:
pg = 980.*9.8 #Peso específico en SI
angulo = 90 #Inclinación de las placas

#Fuerza hidrostática: Fuerza en kN o klb
F = pg  * YC * A *np.sin(angulo*math.pi/180.)/1000

#Imprimiendo resultados
print('XC = %7.5f +- %5.4f' % (XC,0.05*XC))
print('YC = %7.5f +- %5.4f' % (YC,0.05*XC))
print('XP = %7.5f +- %5.4f' % (XP,0.05*XC))
print('YP = %7.5f +- %5.4f' % (YP,0.05*XC))
print('F = %7.5f +- %5.4f' % (F,0.05*XC))

#Graficando
H = H1+H2
v2 = d+c
v3 = v2+b/2
v4 = v3 +b/2
v5 = v4 + c
v6 = v5+d

#Coordenadas
verts = [(0.,0.), (d,-H1), (v2,-H1), (v3,-H), (v4,-H1), (v5,-H1),(v6,0.),(0.,0.)]
codes = [Path.MOVETO,Path.LINETO,Path.LINETO,Path.LINETO,Path.LINETO,Path.LINETO,Path.LINETO, Path.CLOSEPOLY]
#Figura compuesta
path = Path(verts,codes)

#Ploteo de la figura
fig, ax = plt.subplots(figsize=(9,6))

#Poner color a la figura
patch = patches.PathPatch(path, facecolor= 'skyblue', lw=2, alpha=0.4); #alpha:Transparencia
ax.add_patch(patch)

#Ubica con coordenadas punto (Xp,Yp)
plt.plot(XP,-YP,color='black', marker='o', markersize=11)
#Coloca nombre al punto (Xp,Yp)
ax.text(XP+1.3,-YP-1, '(Xp, Yp)',fontsize=12)

#Ubica coordenadas del punto (Xc,Yc)
plt.plot(XP,-YC, color='g', marker='h',markersize=10)
#Coloca nombre al punto (Xc,Yc)
ax.text(XP+1.3,-YC-0.5, '(Xc,YC)', fontsize=12, color='g')

#Ubica los Xc, Yc de cada una de las figuras simples
plt.plot(XP,-5,color='b',marker='.', markersize=12)
plt.plot(XP,-15/2,color='r', marker='.', markersize=12)
plt.plot(XP,-(15+10/3), color='orange', marker='.',markersize=10)

#Coloca límite a la figura
ax.set_xlim(0,B1)
ax.set_ylim(-H,0)

#Agrega la grid
plt.grid(ls='--')

#Bautiza ejes
plt.xlabel('X(m)')
plt.ylabel('H(m)')

plt.show()








