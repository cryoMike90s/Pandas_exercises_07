import pandas as pd

""" Dataset comes from https://www.kaggle.com/nehaprabhavalkar/indian-food-101"""

#Display options
pd.set_option('display.max_rows',500)
pd.set_option('display.min_rows',200)
pd.set_option('display.max_columns',500)
pd.set_option('display.width',1000)
pd.set_option('display.max_colwidth',100)

"""
 Jestes w zespole tworzącym aplikacje webową umożliwiającą generowanie przepisów dań z dostępnych produktów.
 Jesteś odpowiedzialny za stworzenie funkcji generującej przepisy dań kuchni Indyjskiej z dostępnych produktów.
 Dostępne produkty są wprowadzane przez uzytkownika i wczytywane jako lista.

 Przepis musi zawierać wszystkie z podanych przez urzytkownika składników.

"""

df = pd.read_csv('DATA/indian_food/indian_food.csv')
# print(df)


def I_like_this_dish(df, chosen_ingredients, only_selected):
    #First to copy actual df
    df_org = df.copy()

    #Prevention from wrong input
    df['ingredients'] = df['ingredients'].str.upper()

    #Same for created list
    chosen_ingredients = [x.upper() for x in chosen_ingredients]

    #Split the ingredients for every dish
    df['ingredients'] = df['ingredients'].str.split(',')

    #Split rows for every ingredients inside every dish (but same index)
    df = df.explode('ingredients')

    #Prevention from blank spaces and compare choosen ingredients to ingredients from list
    df = df[
        df['ingredients'].str.strip().isin(chosen_ingredients)
    ]

    #Undo the explode "mode"
    df = df.groupby('name', as_index=False).agg({
        'ingredients': (
            lambda x: ','.join(x).split(',')
        )
    })

    #Choose only those dishes which have all ingredients from list
    df = df[
        df['ingredients'].str.len() == len(chosen_ingredients)
    ]

    #Need to depict our output with all columns like prep time etc.
    df_org = df_org[
        df_org['name'].isin(df['name'].tolist())
    ]

    if only_selected:
        df_org = df_org[
            df_org['ingredients'].str.split(',').str.len() == len(chosen_ingredients)
        ]

    print(df_org)


chosen_ingredients = ['flour', 'ghee']
I_like_this_dish(df, chosen_ingredients, False)