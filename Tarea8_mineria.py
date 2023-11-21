import pandas as pd
import matplotlib.pyplot as plt
from typing import Tuple, List
import numpy as np


# Algoritmo de k-means que agrupa los puntos por su "centro de masa" dependiendo de las agrupaciones
def k_means(points: List[np.array], k: int, name: str):
    dim = len(points[0])
    N = len(points)
    num_cluster = k
    iterations = 15

    x = np.array(points)
    y = np.random.randint(0, num_cluster, N)

    mean = np.zeros((num_cluster, dim))
    for t in range(iterations):
        for k in range(num_cluster):
            mean[k] = np.mean(x[y == k], axis=0)
        for i in range(N):
            dist = np.sum((mean - x[i]) ** 2, axis=1)
            pred = np.argmin(dist)
            y[i] = pred

    for kl in range(num_cluster):
        xp = x[y == kl, 0]
        yp = x[y == kl, 1]
        plt.scatter(xp, yp)
    plt.savefig(f"Practica8/{name}.png")
    plt.close()
    return mean


#Lectura del CSV 
df = pd.read_csv("edited-salaries.csv")
# Dataframe que agrupa por temporada y posición y obtiene media del salario
df = df.dropna()
df_mean = df.groupby(['season', 'position'])['salary'].mean().reset_index()
df_mean = df_mean.drop('position', axis=1)
list_t = [
    (np.array(tuples[0:2]), tuples[1])
    for tuples in df_mean.itertuples(index=False, name=None)
]
points = [point for point, _ in list_t]
kn = k_means(
    points,
    4,
    'kmeansposition'
)
print(kn)

#Dataframe que agrupa por temporada y equipo
df = df.dropna()
df_mean = df.groupby(['season', 'team'])['salary'].mean().reset_index()
df_mean = df_mean.drop('team', axis=1)
list_t = [
    (np.array(tuples[0:2]), tuples[1])
    for tuples in df_mean.itertuples(index=False, name=None)
]
points = [point for point, _ in list_t]
kn = k_means(
    points,
    4,
    'kmeansequipo'
)
print(kn)

#Utilizando el datagrame original usamos el salario y la temporada 
eliminar = ['name','position','rank','team','range']
df_rank = df.drop(eliminar, axis=1)
list_t = [
    (np.array(tuples[0:2]), tuples[1])
    for tuples in df_rank.itertuples(index=False, name=None)
]
points = [point for point, _ in list_t]
kn = k_means(
    points,
    4,
    'kmeansgeneral'
)
print(kn)
