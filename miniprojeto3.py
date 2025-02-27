import json

with open('C:/Users/Bruno/Downloads/movies_and_series.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

    series = data['data']['series']
    movies = data['data']['movies']

    max_rating=0
    best_movie=[]

    for movie in movies and series:
        if movie['rating'] > max_rating:
            max_rating = movie['rating']
            best_movie = [movie]

    for movie in best_movie:
        print(f"{movie['title']}")

    print(max_rating)