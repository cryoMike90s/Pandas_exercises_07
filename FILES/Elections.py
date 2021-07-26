import pandas as pd

"""Dataset comes from https://www.kaggle.com/unanimad/us-election-2020"""

#Display options
pd.set_option('display.max_rows',500)
pd.set_option('display.min_rows',200)
pd.set_option('display.max_columns',500)
pd.set_option('display.width',1000)
pd.set_option('display.max_colwidth',100)

"""
zad. 1 Nazwa stanów z największą i najmniejszą ilością ukończonych liczeń głosów [%]
zad. 2 Sprawdzanie średniej procentowej dla stanu Indiana
zad. 3 Stworzenie ramki danych ze średnią procentową postępu,
 oraz minimalna wartość aktualnych głosów dla każdego stanu
zad. 4 Zmiana nazw stanów na duże litery
zad. 5 Zapisywanie wyników zadania nr 3 jako plik csv 
"""

""" Original data load"""

df = pd.read_csv("DATA/elections/governors_county.csv")


# Ex. 1


def check_max_min():
    #Check if our percentage rates are correct
    df['percent_checked'] = ((df['current_votes']/df['total_votes'])*100).round(2)

    #Sort values for better data view
    df_sorted = df.sort_values(by='percent_checked', ascending=False)

    #After analysis of wrong percentage rates comes from data, those need to be thrown away
    df_sorted = df_sorted[df_sorted['percent_checked'] <= 100]

    #All rows with the higest and te lowest percentage
    df_sorted_max = df_sorted[df_sorted['percent_checked'] == df_sorted['percent_checked'].max()]
    df_sorted_min = df_sorted[df_sorted['percent_checked'] == df_sorted['percent_checked'].min()]

    #List all states with max and min percentage of votes
    states_max = set(df_sorted_max['state'].tolist())
    states_min = set(df_sorted_min['state'].tolist())
    return states_max, states_min


# Ex. 2


def check_indiana():
    #Selection only for "Indiana" state
    indiana = df[df['state'] == 'Indiana']
    #Calculation of mean from all values
    indiana_mean = indiana['percent'].mean().round(2)
    return indiana_mean


# Ex. 3


def Ex_3():
    #Check if our percentage rates are correct
    df['percent_checked'] = ((df['current_votes']/df['total_votes'])*100).round(2)

    #Sort values for better data view
    df_sorted = df.sort_values(by='percent_checked', ascending=False)

    #After analysis of wrong percentage rates comes from data, those need to be thrown away
    df_sorted = df_sorted[df_sorted['percent_checked'] <= 100]

    df_state_sort = df_sorted.sort_values(by='state')

    # Final groupby with agg to obtain county in state with the lowest number of votes and to
    # get percentage mean for state

    final_df = df_state_sort.groupby('state').agg({'current_votes': 'min','percent_checked': 'mean'}).round(2)

    return final_df


# Ex. 4


def upper_case():
    df['state']= df['state'].str.upper()
    return df




print(check_max_min())
print(check_indiana())
print(Ex_3())
print(upper_case())

