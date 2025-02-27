import json

with open('C:/Users/Bruno/Downloads/movies_and_series.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

    movies = data["data"]["movies"]

    best_picture_nominees = {}

    for movie in movies:
        for award in movie.get('awards', []):
            if award['category'] == 'Best Picture':
                year = award['year']
                nominees = award.get('nominees', [])
                if year not in best_picture_nominees:
                    best_picture_nominees[year] = []
                best_picture_nominees[year].extend(nominees)



    for year, nominees in sorted(best_picture_nominees.items()):
        print(f"{year}: {', '.join(nominees)}")