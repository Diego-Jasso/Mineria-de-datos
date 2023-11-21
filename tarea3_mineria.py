import pandas as pd
from tabulate import tabulate

#Funcion para imprimir el inicio del df
def print_tabulate(df: pd.DataFrame):
    print(tabulate(df, headers=df.columns, tablefmt='orgtbl'))

#leemos el csv
df = pd.read_csv("edited-salaries.csv")

#salarios de cada equipo en cada temporada
df_by_team = df.groupby(["team","season"]).agg({'salary': ['sum','count','mean','min','max']})
df_by_team = df_by_team.reset_index()
print_tabulate(df_by_team.head())
df_by_team.to_csv('Practica3/salaries_per_team.csv',index = False)

#salarios por cada temporada
df_by_sea = df.groupby(["season"]).agg({'salary': ['sum','count','mean','min','max']})
df_by_sea = df_by_sea.reset_index()
print_tabulate(df_by_sea.head())
df_by_sea.to_csv('Practica3/salaries_per_season.csv',index = False)

#salarios de cada posicion por temporada
df_by_pos = df.groupby(["season","position"]).agg({'salary': ['sum','count','mean','min','max']})
df_by_pos = df_by_pos.reset_index()
print_tabulate(df_by_pos.head())
df_by_pos.to_csv('Practica3/salaries_per_pos.csv',index = False)

#salarios totales de cada posicion 
df_by_postot = df.groupby(["position"]).agg({'salary': ['sum','count','mean','min','max']})
df_by_postot = df_by_postot.reset_index()
print_tabulate(df_by_postot.head())
df_by_postot.to_csv('Practica3/salaries_per_pos_total.csv',index = False)

#salarios totales de cada posicion por equipo
df_by_posteam = df.groupby(["team","position"]).agg({'salary': ['sum','count','mean','min','max']})
df_by_posteam = df_by_posteam.reset_index()
print_tabulate(df_by_posteam.head
df_by_posteam.to_csv('Practica3/salaries_per_pos_per_team.csv',index = False)
