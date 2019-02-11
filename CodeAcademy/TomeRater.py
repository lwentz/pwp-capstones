

class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}

    def read_book(book, rating=None):
        User.books['book'] = rating
        return User.books

    def get_email(self, email):
        self.email = email
        return self.email
    
    def change_email(self, email):
        self.email = email
        print("User's email has been updated.")
        
    def __repr__(self):
        #count the number of books in dictionary str(len(self.books.keys()))
        return "User  " + self.email + " books read: " + str(len(self.books.keys()))
    
    def __eq__(self, other_user):
      if not other_user:
            return False

    def get_average_rating(self):
        count = 0
        _sum = 0
        _avg = 0

        for key in self.books:
            count +=1
            _sum += self.books[key]
        _avg = _sum/count
        return _avg


class Book:
    def __init__(self, title, isbn):
        self.title = title #string
        self.isbn = isbn #number
        self.ratings = []

    def get_title(self, title):
            self.title = title
            return self.title

    def get_isbn(self, isbn):
        self.isbn = isbn
        return self.isbn

    def set_isbn(self, isbn):
        self.isbn = isbn
        print("This {0}, has been updated.".format(isbn))

    def __repr__(self):
        print("The book " + self.isbn + " has been updated.")

    def add_rating(rating):
        if rating > 0 or rating <=4:
            rating.append(rating)
        else:
            print("Invalid Rating")

    def get_average_rating(self):
        count = 0
        _sum = 0
        _avg = 0

        for key in  self.ratings:
            count += 1
            _sum += self.ratings[key]
        _avg = _sum / count
        return _avg

    def __eq__(self, other):
        if not other:
            return False

        return self.title == other.title and self.isbn == other.isbn

    def __hash__(self):
        return hash((self.title, self.isbn))

    
class Fiction(Book):
    def __int__(self, title, author, isbn):
        super().__init__(title, isbn)
        self.author = self.get_author()

    def get_author(self):
        return self.author
    
    def __repr__(self):
        return self.title + " by " + self.author

    
class Non_Fiction(Book):
    def __int__(self, title, subject, level, isbn):
        super().__init__(title, isbn)
        self.subject = self.get_subject()
        self.level = self.get_level()

    def get_subject(self):
        return  self.subject
    
    def get_level(self):
        return self.level
    
    def __repr__(self):
        return self.title + ' a ' + self.level + ' manual on ' + self.subject


class Tome_Rater:
    def __init__(self):
        self.users = {}
        self.books = {}

    def create_book(title, isbn):
        bk = Book(title,isbn)
        return bk

    def create_novel( title, author, isbn):
        fictbk = Fiction(title, isbn)
        return fictbk

    def create_non_fiction(title, subject, level, isbn):
        nonFictionBook = Non_Fiction(title, isbn)
        return nonFictionBook

    def add_book_to_user(book, email, rating=None):
        classtr = Tome_Rater()

        for item in classtr.users:
            if "email" in item:
                User.read_book(item, rating)
                Book.add_rating(rating)
            else:
                print("No user with email " + email)
            if book in classtr.books:
                classtr.books['book']= 1
            else:
                classtr.books['book'] +=1

    def add_user(name, email, user_books=None):
        newuser ={}
        newuser['name',email] = User(name, email)

        if user_books:
            for bk in user_books:
                newuser['book'] = Tome_Rater.add_book_to_user(user_books,email)

    def print_catalog(self):
        for k,v in self.books:
            print(v)

    def print_users(self):
        for k,v in self.users:
            print(v)

    def most_read_book(self,books):
        v=list(books.values)
        k=list(books.keys())
        return k[v.index(max(v))]

    def highest_rated_book(self):
        v=list(Book.get_average_rating().values)
        k=list(Book.get_average_rating().keys())
        return k[v.index(max(v))]

    def most_positive_user(self):
        v=list(User.get_average_rating().values)
        k=list(User.get_average_rating().keys())
        return k[v.index(max(v))]


