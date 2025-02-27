import json
with open('C:/Users/Bruno/Downloads/movies_and_series.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

    series = data['data']['series']
    movies = data['data']['movies']

    biggest_revenue = 0
    top_movie_title = None
    titles = [movie['title']for movie in movies]

    for movie in movies:
        revenue = movie["production"]["boxOffice"]["revenue"]
        if revenue > biggest_revenue:
            biggest_revenue = revenue
            top_movie_title = movie['title']


    print(top_movie_title)
    print(f"Revenue of USD {biggest_revenue}")