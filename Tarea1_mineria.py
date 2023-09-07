import pandas as pd #importamos pandas 
url = "https://raw.githubusercontent.com/erikgregorywebb/datasets/master/nba-salaries.csv" #escribimos la url de nuestro csv


df = pd.read_csv(url) #creamos un dataframe con pandas para ver nuestro url
df.to_csv('nba-salaries.csv', index =False) #lo descargamos en forma de df con index falsos para que no tenga formato y listo