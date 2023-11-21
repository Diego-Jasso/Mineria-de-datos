import pandas as pd #importamos pandas

#Reemplazamos las posiciones por sus nombres completos en vez de abreviaciones
def categorize(position:str)->str:
    if 'C' in position:
        return 'Center'
    if 'PG' in position:
        return 'Point Guard'
    if 'SF' in position:
        return 'Small Forward'
    if 'PF' in position:
        return 'Power Forward'
    if 'SG' in position:
        return 'Shooting Guard'
    if 'G' in position:
        return 'Guard'
    if 'PF' in position:
        return 'Point Forward'
    if 'FC' in position:
        return 'Forward Center'
    if 'F' in position:
        return 'Forward'
    if 'S' in position:
        return 'Swingman'

#Creamos una nueva columna donde clasificamos el salario de cada jugador
def categorizesalary(salary:int)->str:
    if salary<1000000:
        return 'Below 1 million'
    if salary>=1000000 and salary <5000000:
        return 'Above 1 million'
    if salary>=5000000 and salary <10000000:
        return 'Above 5 million'
    if salary>=10000000 and salary <15000000:
        return 'Above 10 million'
    if salary>=15000000:
        return 'Above 15 million'
    

#Leemos el csv que generamos y lo editamos y guardamos con un nuevo nombre
df= pd.read_csv("nba-salaries.csv")
range = df['salary']
df['range'] = range.map(categorizesalary)
position = df['position']
newpos = position.map(categorize)
df['position'] = newpos
df.to_csv('edited-salaries.csv',index = False)
print(df.head())
