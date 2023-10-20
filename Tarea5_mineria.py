import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols

df = pd.read_csv("edited-salaries.csv")

#anova de salarios de cada equipo por temporada
df_by_team = df.groupby(["team","season"])[['salary']].sum()
df_by_team.reset_index(inplace=True)
print(df_by_team.head())

model = ols("salary ~ season", data=df_by_team).fit()
anovaDF = sm.stats.anova_lm(model, typ=2)
if anovaDF["PR(>F)"][0] < 0.005:
    print("Hay diferencia en los salarios de cada equipo por temporada")
    print(anovaDF)
else:
    print("No hay diferencias en los salarios de cada equipo por temporada")

#anova de salarios totales de cada posicion entre los diferentes equipos
df_by_pos= df.groupby(["position","team"])[['salary']].sum()
df_by_pos.reset_index(inplace=True)

print(df_by_pos.head())

model = ols("salary ~ position", data=df_by_pos).fit()
anovaDF = sm.stats.anova_lm(model, typ=2)
if anovaDF["PR(>F)"][0] < 0.005:
    print("Hay diferencia en los salarios de cada posicion entre los equipos")
    print(anovaDF)
else:
    print("No hay diferencias en los salarios de cada posicion entre los equipos")

#anova de salarios totales de cada posicion entre las diferentes temporadas
df_by_num= df.groupby(["season","position"])[("salary")].sum()
#df_by_num.reset_index(inplace=True)

print(df_by_num.head())

model = ols("salary ~ position", data=df_by_pos).fit()
anovaDF = sm.stats.anova_lm(model, typ=2)
if anovaDF["PR(>F)"][0] < 0.005:
    print("Hay diferencia en los salarios de cada posicion en cada temporada")
    print(anovaDF)
else:
    print("No hay diferencias en los salarios de cada posicion en cada temporada")
    