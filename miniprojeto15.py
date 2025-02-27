import json
with open('C:/Users/Bruno/Downloads/movies_and_series.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

    movies = data['data']['movies']

    tickets_domestic = [movies['production']['boxOffice']['ticketSales']['domestic'] for movies in movies]
    tickets_international = [movies['production']['boxOffice']['ticketSales']['international'] for movies in movies]

    for movie in movies:
        print(f"{movie['title']}")
        for i in tickets_domestic:
            print(i)
        for j in tickets_international:
            print(j)