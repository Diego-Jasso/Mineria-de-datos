from wordcloud import WordCloud
from collections import Counter
import matplotlib.pyplot as plt
import pandas as pd


# Abre un archivo con texto y se utiliza el encoder utf-8 para que acepte todo tipo de valores
def open_file(path: str) -> str:
    content = ""
    with open(path, encoding='utf-8') as f:
        content = f.readlines()
    return " ".join(content)


# Abre cierta columna del dataframe y lee sus valores, en caso de no existir dicha columna arroja error
def open_dataframe_column(df: pd.DataFrame, column_name: str) -> str:
    # Verificar si la columna existe en el DataFrame
    if column_name not in df.columns:
        raise ValueError(f"La columna '{column_name}' no existe en el DataFrame.")
    content = " ".join(df[column_name].astype(str))
    return content


# Word cloud con un archivo txt con datos de la portada de la siguiente liga https://cnnespanol.cnn.com
total_words = ""
texto = open_file("noticias.txt")
palabras = texto.rstrip().split(" ")
# Ciclo para encontrar la palabra más repetida
for arg in palabras:
    tokens = arg.split()
    total_words += " ".join(tokens) + " "
wordcloud = WordCloud(
    background_color="white", min_font_size=5
).generate(total_words)
plt.close()
plt.figure(figsize=(5, 5), facecolor=None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad=0)
plt.savefig("Practica10/noticias.png")
plt.close()

#Wordcloud con la columna de los nombres de los jugadores del csv
df = pd.read_csv("edited-salaries.csv")
palabras = open_dataframe_column(df, 'name')
palabras = " ".join(palabras.split())
wordcloud2 = WordCloud(background_color="white", min_font_size=5).generate(palabras)
plt.close()
plt.figure(figsize=(5, 5), facecolor=None)
plt.imshow(wordcloud2)
plt.axis("off")
plt.tight_layout(pad=0)
plt.savefig("Practica10/palabrasJugadorescsv.png")
plt.close()

