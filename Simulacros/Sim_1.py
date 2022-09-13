import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf
from scipy.interpolate import interp1d

##------------------EJERCICIO FLUJO DE AIRE
# tenemos que y es igual a:
y = np.array([0.005,0.01,0.02,0.04,0.06,0.08])
# u:
u = np.array([0.74,1.51,3.03,6.37,10.21,14.43])
#Realizamos la regresión y hallamos los coeficientes.

Data = {'y':  y,
        'u': u}
dataframe = pd.DataFrame(Data,columns = Data.keys())
olsres2 = smf.ols(formula = 'u ~ I(y) + I(y**3) - 1', data = dataframe).fit()
#el -1 es para indicar que es sin intercepto
coefs = olsres2.params


C1 = round(coefs[0],4)
C2 = round(coefs[1],4)
print('C1 = ' +str(C1)+' s^-1')
print ('C2 = ' +str(C2)+' ft^-2 s^-1')

##ROTACION DE CUERPO CONICO
