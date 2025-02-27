import json

with open('C:/Users/Bruno/Downloads/movies_and_series.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

    series = data['data']['series']
    movies = data['data']['movies']

    overall_top_comment = None
    overall_max_votes = 0
    overall_title = None

    def find_top_comment(reviews):
        top_comment = None
        max_votes = 0

        for review in reviews:
            if review['details']['helpfulVotes'] > max_votes:
                max_votes = review['details']['helpfulVotes']
                top_comment = review

        return top_comment


    for movie in movies:
        if movie['reviews']:
            top_comment = find_top_comment(movie['reviews'])
            if top_comment['details']['helpfulVotes'] > overall_max_votes:
                overall_max_votes = top_comment['details']['helpfulVotes']
                overall_top_comment = top_comment
                overall_title = movie['title']

    for serie in series:
        if serie['reviews']:
            top_comment = find_top_comment(serie['reviews'])
            if top_comment['details']['helpfulVotes'] > overall_max_votes:
                overall_max_votes = top_comment['details']['helpfulVotes']
                overall_top_comment = top_comment
                overall_title = serie['title']

    print(f"Title: {overall_title}")
    print(f"Top Comment: {overall_top_comment['comment']}")
    print(f"User: {overall_top_comment['user']}")
    print(f"Helpful Votes: {overall_top_comment['details']['helpfulVotes']}")