import json

with open('C:/Users/Bruno/Downloads/movies_and_series.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

    series = data['data']['series']
    movies = data['data']['movies']

    genres = set(genre for movie in movies for genre in movie['genres']) and set(genre for serie in series for genre in serie['genres'])

    for genre in genres:
        print(genre)