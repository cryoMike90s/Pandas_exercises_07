import pandas as pd
import os

""" Dataset comes from https://www.kaggle.com/nehaprabhavalkar/indian-food-101"""

#Display options
pd.set_option('display.max_rows',500)
pd.set_option('display.min_rows',200)
pd.set_option('display.max_columns',500)
pd.set_option('display.width',1000)
pd.set_option('display.max_colwidth',100)

"""
Przygotuj funkcje dla Twojej aplikacji webowej która bedzie w stanie przetworzyc
    wszystkie wczytane przez uzytkownika pliki wg wytycznych.

 W folderze znajdują się przepisy zawierajace: przepisy słodkie, ostre oraz reszta ,

  funkcja musi posiadac nastepujace możliwosci:

    1. wygenerowanie pliku zawierajacego wszystkie przepisy dla stanu West Bengal
    2. wygenerowanie pliku z piecioma przepisami które posiadają najdłuższy czas przygotowania
    3. wygenerowanie pliku zawierajacego top 10 najprostszych przepisów pod względem przygotowania (ilosc składników)

 uwaga: przygotować dane do analizy z pliku głównego indian food :)
"""


df = pd.read_csv('DATA/indian_food/indian_food.csv')
# print(df)

#Split data for three files that contains specific flavor: sweet, spicy and rest


lista = ['sweet', 'spicy', 'others']

def save_me():
    for data in lista:
        if data in lista[0:2]:
            a = data
            data = df[df['flavor_profile'] == data]
            data.to_excel(os.path.join('OUTPUT', "indian_food_{}.xlsx".format(a)), engine='openpyxl')
        else:
            data = df[~(df['flavor_profile'] == 'spicy') &
                      ~(df['flavor_profile'] == 'sweet')]
            data.to_excel(os.path.join('OUTPUT', "indian_food_others.xlsx"), engine='openpyxl')


def west():
    west_bengal = df[df['state']=="West Bengal"]
    return west_bengal


def longest_time():
    longest_time_var = df.groupby('name').agg({"prep_time":"max"}).sort_values(by='prep_time',ascending=False)
    return longest_time_var.head()


def ten():
    ingredients = df['ingredients'].tolist()
    final = [[x.strip(' ') for x in ingr.split(',')] for ingr in ingredients]
    df['ingredients'] = final
    df['ingredients_count'] = df['ingredients'].str.len()
    df_sort = df.sort_values(by='ingredients_count', ascending=True)
    return df_sort.head(10)

print(west())
print(longest_time())
print(ten())