import pandas as pd
import matplotlib.pyplot as plt
from typing import Tuple, List
import numpy as np

def get_cmap(n, name="hsv"):
    return plt.cm.get_cmap(name, n)

#funcion para nuestro scatter
def scatter_group_by(
    file_path: str, df: pd.DataFrame, x_column: str, y_column: str, label_column: str
):
    fig, ax = plt.subplots()
    labels = pd.unique(df[label_column])
    cmap = get_cmap(len(labels) + 1)
    for i, label in enumerate(labels):
        filter_df = df.query(f"{label_column} == '{label}'")
        ax.scatter(filter_df[x_column], filter_df[y_column], label=label, color=cmap(i/len(labels)))
    ax.legend()
    plt.savefig(file_path)
    plt.close()

#Funcion para calcular distancia euclideana
def euclidean_distance(p_1: np.array, p_2: np.array) -> float:
    return np.sqrt(np.sum((p_2 - p_1) ** 2))

#funcion para calcular los vecinos mas cercanos
def k_nearest_neightbors(
    points: List[np.array], labels: np.array, input_data: List[np.array], k: int
):
    input_distances = [
        [euclidean_distance(input_point, point) for point in points]
        for input_point in input_data
    ]
    points_k_nearest = [
        np.argsort(input_point_dist)[:k] for input_point_dist in input_distances
    ]
    predicted_labels = [
        np.argmax(np.bincount([label_to_number[labels[index]] for index in point_nearest]))
        for point_nearest in points_k_nearest
    ]
    return predicted_labels


# Leemos el csv 
df = pd.read_csv("edited-salaries.csv")
df_mean = df.groupby(['season','position'])['salary'].mean().reset_index()

label_to_number = {label: i for i, label in enumerate(df_mean['position'].unique())}
number_to_label = {i: label for i, label in enumerate(df_mean['position'].unique())}

#Usamos la funcion de scatter mandando como eje x la temporada, eje y como el salario, y los labels como las posiciones
scatter_group_by("Practica7/positions_scatter.png", df_mean, "season", "salary", "position")
list_t = [
    (np.array(tuples[0:1]), tuples[2])
    for tuples in df.itertuples(index=False, name=None)
]
kn = k_nearest_neightbors(
    df_mean[['salary','season']].to_numpy(),
    df_mean['position'].to_numpy(),
    [np.array([100, 150]), np.array([1, 1]), np.array([1, 300]), np.array([80, 40])],
    5
)
print(kn)

label_to_number = {label: i for i, label in enumerate(df['range'].unique())}
number_to_label = {i: label for i, label in enumerate(df['range'].unique())}

#Llamamos al scatter mandando como eje x el puesto ,eje y como el salario, y los labels que sea el rango del salario
scatter_group_by("Practica7/salaries_scatter.png", df, "rank", "salary", "range")
list_t = [
    (np.array(tuples[0:1]), tuples[2])
    for tuples in df.itertuples(index=False, name=None)
]
kn = k_nearest_neightbors(
    df[['salary','rank']].to_numpy(),
    df['range'].to_numpy(),
    [np.array([100, 150]), np.array([1, 1]), np.array([1, 300]), np.array([80, 40])],
    5
)
print(kn)
