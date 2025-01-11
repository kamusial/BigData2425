import pandas as pd

# wczytywanie danych
df = pd.read_json('data\\dane.json')

# wyświetlanie danych
print("Pierwsze 5 wierszy danych:")
print(df.head())

# filtracja danych
mlodsi_niz_30 = df[df['wiek'] < 30]
print(mlodsi_niz_30)

# dodawanie nowej kolumny
df['wiek_za_5_lat'] = df['wiek'] + 5
print("\nDane z dodaną kolumną 'wiek_za_5_lat':")
print(df)

# statystyka
sredni_wiek = df['wiek'].mean()
print(f'\nŚredni wiek: {sredni_wiek}')

# sortowanie
df_sorted = df.sort_values('wiek', ascending=False)
print("\nDane posortowane po wieku malejąco:")
print(df_sorted)

# export danych
df.to_json('final_data\\json_deafult.json')
df.to_json('final_data\\1json_deafult_indent4.json', indent=4)
df.to_json('final_data\\2json_deafult_indent4_split.json', orient='split', indent=4)
df.to_json('final_data\\3json_deafult_indent4_record.json', orient='records', indent=4)
df.to_json('final_data\\4json_deafult_indent4_index.json', orient='index', indent=4)
df.to_json('final_data\\5json_deafult_indent4_colums.json', orient='columns', indent=4)
df.to_json('final_data\\6json_deafult_indent4_values.json', orient='values', indent=4)
df.to_json('final_data\\7json_deafult_indent4_table.json', orient='table', indent=4)

