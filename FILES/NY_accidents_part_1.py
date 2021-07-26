import pandas as pd


pd.set_option('display.max_rows',500) #ilos rzedow do wyswietlenia (max)
# pd.set_option('display.min_rows',200) # minimalna ilosc rzedow do wyswietlenia (min)
pd.set_option('display.max_columns',500) #ilos kolumn do wyswietlenia (max)
pd.set_option('display.width',1000) #definiowanie szerkokosci kazdej kolumny
pd.set_option('display.max_colwidth',100) #ilosc znakow w kolumnie

"""
Jaki dzień tygodnia to najgorszy dzień, jeżeli chodzi o wypadki dla wszystkich dzielnic w NY?
"""

df = pd.read_csv("DATA/NY_emergency/nypd-motor-vehicle-collisions.csv", usecols=['ACCIDENT DATE', 'ACCIDENT TIME'])
# print(df)

def worst_day():
    df['ACCIDENT DATE'] = pd.to_datetime(df['ACCIDENT DATE']).dt.day_name()
    grouped = df.groupby('ACCIDENT DATE').agg({'ACCIDENT TIME': 'count'})
    grouped = grouped.sort_values(by='ACCIDENT TIME', ascending=False)
    print(grouped)

worst_day()

