import json
with open('C:/Users/Bruno/Downloads/movies_and_series.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

    movies = data['data']['movies']

    all_film_loc = []

    for movie in movies:
        for filmlocations in movie['production']['filmingLocations']:
            all_film_loc.append(filmlocations)


    for location in all_film_loc:
        print(location)