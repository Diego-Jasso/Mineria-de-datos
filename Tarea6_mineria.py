import matplotlib.pyplot as plt
import statsmodels.api as sm
from scipy.stats import spearmanr
from scipy.stats import pearsonr
import pandas as pd

#Regresion del promedio de salario total por temporada
df = pd.read_csv("edited-salaries.csv")
df_mean = df.groupby('season')['salary'].mean().reset_index()
df_mean['season'] = [2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020]

X = sm.add_constant(df_mean['season'])
Y = df_mean['salary']
modelo = sm.OLS(Y, X).fit()
print(modelo.summary())

#Grafica 
plt.figure(figsize=(10, 6))
plt.scatter(df_mean['season'], df_mean['salary'], label='Promedio por temporada')
plt.plot(df_mean['season'], modelo.predict(X), color='red', label='Pendiente de Regresión')
plt.xlabel('Temporadas')
plt.ylabel('Promedio de salario')
plt.title('Regresion lineal: Promedio de salarios totales por temporada')
plt.legend()
plt.savefig("Practica 6/RegresionPorTemporada.png")
plt.tight_layout()
plt.close()
print(df_mean)
# Coefciente de correlación Spearman
predicciones = modelo.predict(sm.add_constant(X))
spearman, p_valor = spearmanr(predicciones, Y)
print("Coeficiente de correlación de Spearman:", spearman)
print("Valor p:", p_valor)
# Coeficiente de correlación Pearson
coeficiente_pearson, p_value = pearsonr(predicciones, Y)
print("Coeficiente de correlación de Pearson:", coeficiente_pearson)
print("Valor p:", p_value)

#Regresion del promedio de salario de cada posicion por temporada
df = pd.read_csv("edited-salaries.csv")
df_mean = df.groupby(['season','position'])['salary'].mean().reset_index()

#Regresion para la posicion de centro
df_pos = df_mean[df_mean['position'] == 'Center']
df_pos['season'] = [2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020]
X = sm.add_constant(df_pos['season'])
Y = df_pos['salary']
modelo = sm.OLS(Y, X).fit()
print(modelo.summary())

#Grafica para la pos de centro
plt.figure(figsize=(10, 6))
plt.scatter(df_pos['season'], df_pos['salary'], label='Promedio por temporada')
plt.plot(df_pos['season'], modelo.predict(X), color='red', label='Pendiente de Regresión')
plt.xlabel('Temporadas')
plt.ylabel('Promedio de salarios para los centros')
plt.title('Regresion lineal: Promedio de salarios de los centros por temporada')
plt.legend()
plt.savefig("Practica 6/RegresionPorPosicion(Centro).png")
plt.tight_layout()
plt.close()
print(df_pos)
# Coefciente de correlación Spearman
predicciones = modelo.predict(sm.add_constant(X))
spearman, p_valor = spearmanr(predicciones, Y)
print("Coeficiente de correlación de Spearman:", spearman)
print("Valor p:", p_valor)
# Coeficiente de correlación Pearson
coeficiente_pearson, p_value = pearsonr(predicciones, Y)
print("Coeficiente de correlación de Pearson:", coeficiente_pearson)
print("Valor p:", p_value)

#Regresion del promedio de salario de cada equipo por temporada
df = pd.read_csv("edited-salaries.csv")
df_mean = df.groupby(['season','team'])['salary'].mean().reset_index()

#Regresion para el equipo de Chicago Bulls
df_team = df_mean[df_mean['team'] == 'Chicago Bulls']
df_team['season'] = [2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020]
X = sm.add_constant(df_team['season'])
Y = df_team['salary']
modelo = sm.OLS(Y, X).fit()
print(modelo.summary())

#Grafica de los Chicago Bulls
plt.figure(figsize=(10, 6))
plt.scatter(df_team['season'], df_team['salary'], label='Promedio por temporada')
plt.plot(df_team['season'], modelo.predict(X), color='red', label='Pendiente de Regresión')
plt.xlabel('Temporadas')
plt.ylabel('Promedio de salarios para Chicago Bulls')
plt.title('Regresion lineal: Promedio de salarios de los Chicago Bulls por temporada')
plt.legend()
plt.savefig("Practica 6/RegresionPorEquipo(Bulls).png")
plt.tight_layout()
plt.close()
print(df_team)
# Coefciente de correlación Spearman
predicciones = modelo.predict(sm.add_constant(X))
spearman, p_valor = spearmanr(predicciones, Y)
print("Coeficiente de correlación de Spearman:", spearman)
print("Valor p:", p_valor)
# Coeficiente de correlación Pearson
coeficiente_pearson, p_value = pearsonr(predicciones, Y)
print("Coeficiente de correlación de Pearson:", coeficiente_pearson)
print("Valor p:", p_value)