import json

with open('C:/Users/Bruno/Downloads/movies_and_series.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

    series = data['data']['series']
    movies = data['data']['movies']

    for movie in movies:
        print(f"{movie['title']}")
        for platform, availability in movie['streaming'].items():
            if availability['available']:
                print(platform)
                print()

    for serie in series:
        print(f"{serie['title']}")
        for platform, availability in serie['streaming'].items():
            if availability['available']:
                print(platform)
                print()