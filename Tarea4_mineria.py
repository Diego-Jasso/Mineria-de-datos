import pandas as pd
import matplotlib.pyplot as plt

#Leer el csv
df = pd.read_csv("edited-salaries.csv")

#Salario por cada equipo grafica de bigotes
df_by_team = df.groupby(["team","season"])[['salary']].mean()
df_by_team.boxplot(by = 'team', figsize=(27,18))
plt.xticks(rotation=90)
plt.savefig("Practica 4/teams.png")
plt.close()

#Salario por cada temporada grafica de bigotes
df_by_sea = df.groupby(["team","season"])[['salary']].mean()
df_by_sea.boxplot(by = 'season', figsize=(27,18))
plt.xticks(rotation=90)
plt.savefig("Practica 4/seasons.png")
plt.close()

#Salario por posicion grafica de bigotes
df_by_pos = df.groupby(["season","position"])[['salary']].mean()
df_by_pos.boxplot(by = 'position', figsize=(27,18))
plt.xticks(rotation=90)
plt.savefig("Practica 4/positions.png")

plt.close()
