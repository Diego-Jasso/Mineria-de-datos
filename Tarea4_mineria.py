import pandas as pd
from tabulate import tabulate
from typing import Tuple, List
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.formula.api import ols


df = pd.read_csv("edited-salaries.csv")

#Salario por cada equipo
df_by_team = df.groupby(["team","season"])[['salary']].mean()
df_by_team.boxplot(by = 'team', figsize=(27,18))
plt.xticks(rotation=90)
plt.savefig("teams.png")
plt.close()

#Salario por cada temporada 
df_by_sea = df.groupby(["team","season"])[['salary']].mean()
df_by_sea.boxplot(by = 'season', figsize=(27,18))
plt.xticks(rotation=90)
plt.savefig("seasons.png")
plt.close()

#Salario por posicion
df_by_pos = df.groupby(["season","position"])[['salary']].mean()
df_by_pos.boxplot(by = 'position', figsize=(27,18))
plt.xticks(rotation=90)
plt.savefig("positions.png")
plt.close()
