
# filename = "given_files/" + "a_example.txt"
filename = "given_files/" + "b_read_on.txt"

# import os

# os.system("ls")

def load_txt_file(path):
    with open(path) as fin:
        return fin.read()
        # print(text)


class Universe:
    def __init__(self, total_books, n_libraries, n_days, libraries):
        self.total_books = total_books
        self.n_libraries = n_libraries
        self.n_days = n_days
        self.libraries = libraries 

class Library:
    def __init__(self, n_books, signup_time, shiping_rate, books):
        self.n_books = n_books
        self.signup_time = signup_time
        self.shiping_rate = shiping_rate
        self.books = books      # a collection of Book objects

class Book:
    def __init__(self, id, score):
        self.id = id
        self.score = score



def build_universe(filename):
    text = load_txt_file(filename)
    
    
    token = text.split("\n")
    for i in range(0, len(token)):
        token[i] = token[i].split(" ")
    total_books = int(token[0][0])
    n_libraries = int(token[0][1])
    n_days = int(token[0][2])
    
    book_scores = token[1]
    for i in range(0, len(book_scores)):
        book_scores[i] = int(book_scores[i])
    
    # print(n_libraries)
    # print()
    
    
    libraries = []
    for i in range(2, len(token), 2):
        i_pp = i + 1
        
        # print(len(token[i_pp]))
        # if len(token[i]) == 0:
        #     break
        # print(len(libraries) + 1, (len(libraries) + 1) == n_libraries, end="\t")
        
        if ((len(libraries)) == n_libraries):
            break
        
        n_books = int(token[i][0])
        signup_time = int(token[i][1])
        shiping_rate = int(token[i][2])
        
        books = []
        for j in range(0, len(token[i_pp])):
            book_id = int(token[i_pp][j])
            # print(book_id, end=" ")
            book_score = book_scores[book_id]
            
            books.append(Book(book_id, book_score))
            
            
        libraries.append(Library(n_books, signup_time, shiping_rate, books))
        
        print()
        
    return Universe(total_books, n_libraries, n_days, libraries)



        
#=================
# Print universe hacky

def test_and_print_example():
    univ = build_universe(filename)
    assert type(univ.total_books) == int
    assert type(univ.n_libraries) == int
    assert type(univ.n_days) == int
    for lib in univ.libraries:
        assert type(lib.n_books) == int
        assert type(lib.shiping_rate) == int
        assert type(lib.signup_time) == int
        print(lib.n_books, lib.signup_time, lib.shiping_rate)
        print("\t", end="")
        for book in lib.books:
            assert type(book.id) == int
            assert type(book.score) == int
            print("(" + str(book.id) +","+ str(book.score) + ")", end=" ")
        print()
        print()
    
#=================


