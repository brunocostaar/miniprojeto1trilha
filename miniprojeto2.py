import json

with open('C:/Users/Bruno/Downloads/movies_and_series.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

    series = data['data']['series']

    titles = [serie['title']for serie in series]

    for i in titles:
        print(i)