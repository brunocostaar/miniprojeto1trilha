import json
with open('C:/Users/Bruno/Downloads/movies_and_series.json', 'r' ,encoding='utf-8' ) as file:
    data = json.load(file)

series = data['data']['series']
movies = data['data']['movies']
actors_list = []


for series in series:
    for cast in series['cast']:
        actors_list.append(f'{cast['actor']} → {cast['character']}')

for movie in movies:
    for cast in movie['cast']:
        actors_list.append(f'{cast['actor']} → { cast['character']}')

    for i in actors_list:
        print(i)