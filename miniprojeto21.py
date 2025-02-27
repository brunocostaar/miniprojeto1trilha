import json
from datetime import datetime

with open('C:/Users/Bruno/Downloads/movies_and_series.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

    series = data['data']['series']
    movies = data['data']['movies']


    def filter_reviews_before_2022(reviews):
        filtered_reviews = []
        for review in reviews:
            review_date = datetime.strptime(review['details']['date'], "%Y-%m-%d")
            if review_date.year < 2022:
                filtered_reviews.append(review)
        return filtered_reviews


    for movie in movies:
        if movie['reviews']:
            filtered_reviews = filter_reviews_before_2022(movie['reviews'])
            if filtered_reviews:
                print(f"Title: {movie['title']}")
                for review in filtered_reviews:
                    print(f"User: {review['user']}")
                    print(f"Comment: {review['comment']}")
                    print(f"Date: {review['details']['date']}")
                    print(f"Helpful votes: {review['details']['helpfulVotes']}\n")

    for serie in series:
        if serie['reviews']:
            filtered_reviews = filter_reviews_before_2022(serie['reviews'])
            if filtered_reviews:
                print(f"Title: {serie['title']}")
                for review in filtered_reviews:
                    print(f"User: {review['user']}")
                    print(f"Comment: {review['comment']}")
                    print(f"Date: {review['details']['date']}")
                    print(f"Helpful votes: {review['details']['helpfulVotes']}")