import json
with open('C:/Users/Bruno/Downloads/movies_and_series.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

movies = data['data']['movies']
titles = [movie['title']for movie in movies]

for movies in movies:
    for director in movies['directors']:
        print(director)