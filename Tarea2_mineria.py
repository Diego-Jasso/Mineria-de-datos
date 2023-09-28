import pandas as pd #importamos pandas

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
    
df= pd.read_csv("nba-salaries.csv")
print(df.head())
position = df['position']
newpos = position.map(categorize)
df['position'] = newpos
df.to_csv('edited-salaries.csv',index = False)

