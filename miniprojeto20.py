import json

with open('C:/Users/Bruno/Downloads/movies_and_series.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

    series = data['data']['series']
    movies = data['data']['movies']

    total_rating = sum(movie['rating'] for movie in movies)
    average_rating = total_rating / len(movies)

    print(f"Movies rating average: {average_rating:.2f}")