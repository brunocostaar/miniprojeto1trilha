import json
with open('C:/Users/Bruno/Downloads/movies_and_series.json', encoding='utf-8') as file:
    data = json.load(file)

    series = data['data']['series']
    movies = data['data']['movies']


    profit_sum = sum([movie["production"]["boxOffice"]["profit"] for movie in movies])
    profit_average = profit_sum/len(movies)

    print(f"Movies profit average: {profit_average}")