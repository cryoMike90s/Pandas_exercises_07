import pandas as pd
from datetime import datetime


pd.set_option('display.max_rows',500) #ilos rzedow do wyswietlenia (max)
# pd.set_option('display.min_rows',200) # minimalna ilosc rzedow do wyswietlenia (min)
pd.set_option('display.max_columns',500) #ilos kolumn do wyswietlenia (max)
pd.set_option('display.width',1000) #definiowanie szerkokosci kazdej kolumny
pd.set_option('display.max_colwidth',100) #ilosc znakow w kolumnie

"""
 Zad 2. 
 Stworz na podstawie dostarczonych danych, które są ciągle updatowane, 
    funkcje która umożliwi wygenerowanie raportu, dotyczącego podsumowania stłuczek w danym rejonie NY.

    wymaganie 1. Raport ma być wygenerowany dla podanego przedziału czasowego podanego przez usera w formacie :
        %YYYY-%MM-%DD

    wymaganie 2. Raport dostarczony do usera powinien pokazac typ pojazdu który najczęściej brał udział w wypadkach,
    dla danej dzielnicy NY w określonym przedziale czasowym.


      2. Raport powinien zawierać :
        - date wypadku
        - dzielnice
        - typ pojazdu biorącego udział w wypadku   
"""

df = pd.read_csv("DATA/NY_emergency/nypd-motor-vehicle-collisions.csv", usecols=[
    'ACCIDENT DATE','BOROUGH', 'VEHICLE TYPE CODE 1', 'VEHICLE TYPE CODE 2', 'VEHICLE TYPE CODE 3']
)


def raport(dates):
    cleaned = df.copy()

    cleaned = cleaned.dropna(subset=['BOROUGH'])

    vehicles = ['VEHICLE TYPE CODE 1', 'VEHICLE TYPE CODE 2', 'VEHICLE TYPE CODE 3']

    for x in vehicles:
        cleaned[x] = cleaned[x].str.upper()

    cleaned['ACCIDENT DATE'] = pd.to_datetime(cleaned['ACCIDENT DATE']).dt.date

    cleaned = cleaned.sort_values(by=['ACCIDENT DATE'])

    cleaned = cleaned[
        (cleaned["ACCIDENT DATE"] >= dates[0]) &
        (cleaned["ACCIDENT DATE"] <= dates[1])
    ]

    auto = cleaned.groupby(
        ['BOROUGH', 'VEHICLE TYPE CODE 1']
    )['VEHICLE TYPE CODE 1'].count().reset_index(name='count')

    autox = auto.groupby('BOROUGH').agg({
        'count':'idxmax'
    })

    auto = auto.iloc[
        autox['count'].tolist()
    ]

    print(auto)


def give_me_time():
    dates_str = ['2019/07/01', '2019/07/10']
    dates = []

    for date in dates_str:
        date = datetime.strptime(date, '%Y/%m/%d').date()
        dates.append(date)
    return dates


raport(give_me_time())