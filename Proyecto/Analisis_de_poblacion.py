import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
 
"Importacion de datos como referencia"
url = 'https://raw.githubusercontent.com/lorey/list-of-countries/master/csv/countries.csv'
df = pd.read_csv(url, sep=";")
print(df.head(5))


"Impresion de datos basicos en Pandas"
"Nombres de columnas y contenidos"
print('Cantidad de Filas y columnas:',df.shape)
print('Nombre columnas:',df.columns)

"Despliegue de Informacion con objetos vacios"
df.info()

"Descripción estadística de los datos numéricos"
df.describe()

"Utilizar Pandas para encontrar correlacion entre los datos"
corr = df.set_index('alpha_3').corr()
sm.graphics.plot_corr(corr, xnames=list(corr.columns))
plt.show()

"Debido a la poca relacion que tienen entre ambos Archivos. Se decide cargar otro archivo CSV para"
"ahondar el crecimiento de la poblacion"
url = 'https://raw.githubusercontent.com/DrueStaples/Population_Growth/master/countries.csv'
df_pop = pd.read_csv(url)
print(df_pop.head(5))
df_pop_es = df_pop[df_pop["country"] == 'Spain' ]
print(df_pop_es.head())
df_pop_es.drop(['country'],axis=1)['population'].plot(kind='bar')

"Se hara una comparacion entre dos paises, por lo que es necesario comentar la linea 32 a 35"
df_pop_ar = df_pop[(df_pop["country"] == 'Argentina')]
 
anios = df_pop_es['year'].unique()
pop_ar = df_pop_ar['population'].values
pop_es = df_pop_es['population'].values
 
df_plot = pd.DataFrame({'Argentina': pop_ar,
'Spain': pop_es}, 
index=anios)
df_plot.plot(kind='bar')

"Filtracion de Paises de habla hispana"
df_espanol = df.replace(np.nan, '', regex=True)
df_espanol = df_espanol[ df_espanol['languages'].str.contains('es') ]
df_espanol