import parser_2 as parser

filename = "given_files/" + "a_example.txt"
# filename = "given_files/" + "b_read_on.txt"
# filename = "given_files/" + "c_incunabula.txt"

u = parser.build_universe(filename)

book_score_pairs = []
for i in range(0, u.total_books):
    # print((i, u.scores[i]))
    book_score_pairs.append((i, u.scores[i]))
    
# book_score_pairs = [(i, )]

def lib_score(lib, book_score_pairs, days_left):
    # lib.books.sort()          # no need now just use number of books
    
    days_left_after_signup = days_left - lib.signup_time
    return min(days_left_after_signup * 1, lib.n_books)



# a = 2
# print(u.libraries[a].signup_time)
# print(lib_score(u.libraries[a], book_score_pairs, u.n_days))


def get_best_lib(book_score_pairs, days_left):
    max_i = 0
    max_v = 0
    for i in range(0, len(u.libraries)):
        v = lib_score(u.libraries[i], book_score_pairs, days_left)
        if v > max_v:
            max_v = v
            max_i = i

    return max_i

def get_reachable_books(book_score_pairs, lib_index, days_left):
    return u.libraries[lib_index].books[0:min(days_left, u.libraries[lib_index].n_books)]

def remove_lib_books(book_score_pairs, best_lib_index, days_left):
    # best_lib_books = u.libraries[best_lib_index].books
    best_lib_books = get_reachable_books(book_score_pairs, best_lib_index, days_left)
    
    for b in best_lib_books:
        # book_score_pairs.pop()
        # for bp in book_score_pairs:
        #     if 
        
        for bp in book_score_pairs:
            if bp[0] == b:
                book_score_pairs.remove(bp)
    
    return book_score_pairs


days_left = u.n_days
best_libs = []
book_ids = []
while days_left >= 0:
    bl = get_best_lib(book_score_pairs, u.n_days)
    best_libs.append(bl)
    book_ids.append(get_reachable_books(book_score_pairs, bl, days_left))
    
    
    days_left -= u.libraries[bl].signup_time
    
    book_score_pairs = remove_lib_books(book_score_pairs, bl, days_left)
    u.libraries.pop(bl)
    u.n_libraries -= 1
    
    
# print("hi")
print(best_libs)
print(book_ids)
    

# bl = get_best_lib(u, book_score_pairs, u.n_days)
# nbsp = remove_lib_books(u, book_score_pairs, bl)
# print(nbsp)
