import json

with open('C:/Users/Bruno/Downloads/movies_and_series.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

    series = data['data']['series']
    movies = data['data']['movies']

    salarys = []
    bigger_salary_mov = 0
    bigger_salary_ser = 0
    highest_paid_mov = None
    highest_paid_ser = None

    for movies in movies:
        for cast in movies['cast']:
            if cast['salary'] > bigger_salary_mov:
                bigger_salary_mov = cast['salary']
                highest_paid_mov = cast['actor']

    for series in series:
        for cast in series['cast']:
            if cast['salary'] > bigger_salary_ser:
                bigger_salary_ser = cast['salary']
                highest_paid_ser = cast['actor']

    print(f"The highest movies salary is : USD {bigger_salary_mov}, and it belongs to: {highest_paid_mov}")
    print(f"The highest series salary is : USD {bigger_salary_ser}, and it belongs to: {highest_paid_ser}")