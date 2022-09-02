import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf
from scipy.interpolate import interp1d
# tenemos que y es igual a:
y = np.array([0.005,0.01,0.02,0.04,0.06,0.08])

# u:
u = np.array([0.72,1.56,3.43,6.07,11.11,17.04])
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

ecuacion = interp1d(y, u, kind="cubic")

X=np.linspace(np.min(y),np.max(y),500)
Y= ecuacion(X)
etiqueta = 'u='+str(C1)+'y+'+str(C2)+'$y^{3}$'

plt.figure()
plt.title('Perfil de velocidades')
plt.plot(y, u, marker='.', color='k', ls='', label='Datos experimentales')
plt.plot(X, Y, color='r', ls='--', label=etiqueta)
plt.grid(ls='--')
plt.xlabel('y (pie)')
plt.ylabel('Velocidad (pie/s)')
plt.legend()
plt.savefig('Perfil_velocidades_quiznum.pdf',dpi=150)
plt.show()
plt.close()

perf_1 =C1*(0.070)+C2*(0.070**3)
print(f'El perfil de velocidad a los 0.070 pies de altura es= {perf_1}')