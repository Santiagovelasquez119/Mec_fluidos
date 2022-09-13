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





