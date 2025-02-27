import json
with open('C:/Users/Bruno/Downloads/movies_and_series.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

    movies = data['data']['movies']
    series = data['data']['series']

    winners =  []

    for movies in movies:
        for award in movies.get('awards', []):
            if award.get('won'):
                winners.append(f"{movies['title']} ({award['year']}): {award['award']} - {award['category']}")


    for series in series:
        for award in series.get('awards', []):
            if award.get('won'):
                winners.append(f"{series['title']} ({award['year']}): {award['award']} - {award['category']}")

    for i in winners:
        print(i)