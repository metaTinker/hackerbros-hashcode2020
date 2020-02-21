import operator
from parser import Library

def sort_books(books):
    return sorted(books, key=operator.attrgetter('score'))

def max_score(library: Library, days: int, remaining_books):
    max_score = 0
    days_necessary = library.signup_time
    current_day = 0
    for b in sort_books(library.books):
        if b in remaining_books and current_day > days_necessary and current_day < days:
            max_score += b.score
            current_day += 1

    return max_score

def bottom_up(days: int, libraries):
    lib_score_per_day = [[0]]
    libraries_left = libraries
    for j in range(days):
        for i in range(len(libraries)):
            if j > libraries[i].signup_time:
                books = sort_books(libraries[i])
                lib_score_per_day[i][j] = max_score(i, days-j, 0)

    print(lib_score_per_day)

bottom_up()








