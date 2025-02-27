import json

with open('C:/Users/Bruno/Downloads/movies_and_series.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

    series = data['data']['series']
    movies = data['data']['movies']

    fourk_movies = []
    fourk_series = []

    for movie in movies:
        for res in movie['streaming']['Netflix']['resolution']:
            if res=="4K":
                fourk_movies.append(movie)

    for serie in series:
        for res in serie['streaming']['Netflix']['resolution']:
            if res=="4K":
                fourk_series.append(serie)

    for movie in fourk_movies:
        print(f"{movie['title']}")

    for serie in fourk_series:
        print(f"{serie['title']}")