import numbers
from typing import Dict
import matplotlib.pyplot as plt
import pandas as pd
import statsmodels.api as sm


# Función para obtebner las x númericas, donde si originalmente no son númericas, se transforman en éstas
def transform_variable(df: pd.DataFrame, x:str) -> pd.Series:
    if isinstance(df[x][0], numbers.Number):
        return df[x] # type: pd.Series
    else:
        return pd.Series([i for i in range(0, len(df[x]))])


# Creación de la regresión lineal principal donde se crean tambien los rangos menor y mayor
def linear_reg(df: pd.DataFrame, x:str, y: str) -> Dict[str, float]:
    fixed_x = transform_variable(df, x)
    model = sm.OLS(df[y],sm.add_constant(fixed_x)).fit()
    print(model.summary())
    coef = model.params
    m = coef.values[1]
    b = coef.values[0]
    r_2_t_df = pd.DataFrame(model.summary().tables[0])
    r2 = r_2_t_df.values[0][3]
    r2_adj = r_2_t_df.values[1][3]
    band_table = model.summary().tables[1][1]
    lb = str(band_table[5])
    lb = float(lb)
    hb = str(band_table[6])
    hb = float(hb)
    return {'m': m, 'b': b, 'r2': r2, 'r2_adj': r2_adj, 'low_band': lb, 'hi_band': hb}


# Funcion para crear un plot tipo scatter donde vamos a predecir
def plt_lr(df: pd.DataFrame, x:str, y: str, m: float, b: float, r2: float, r2_adj: float, low_band: float, hi_band: float):
    fixed_x = transform_variable(df, x)
    df.plot(x=x,y=y, kind='scatter')
    plt.plot(df[x],[m * x + b for _, x in fixed_x.items()], color='green')
    plt.fill_between(df[x], [m * x + low_band for _, x in fixed_x.items()], [m * x + hi_band for _, x in fixed_x.items()], alpha=0.5, color='red')


# Lectura del dataframe 
df = pd.read_csv("edited-salaries.csv")
# Prediccion para los salarios de cada temporada
eliminar = ['team','rank','position','range','name']
df_mean = df.drop(eliminar, axis=1)
df_mean.reset_index(inplace=True)
df_mean = df_mean.dropna()
lin = linear_reg(df_mean, "season", "salary")
plt_lr(df=df_mean, x="season", y="salary", **lin)
plt.xticks(rotation=90)
plt.savefig('Practica9/prediccionSalariopromedio.png')
plt.close()


