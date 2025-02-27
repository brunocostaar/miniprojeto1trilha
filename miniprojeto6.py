import json

with open('C:/Users/Bruno/Downloads/movies_and_series.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

    series = data['data']['series']
    movies = data['data']['movies']

    platforms = set()

    for movie in movies:
        for platform in movie['streaming']:
            platforms.add(platform)

    for serie in series:
        for platform in serie['streaming']:
            platforms.add(platform)

    for platform in platforms:
        print(platform)