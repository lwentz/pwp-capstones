

class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}

    def read_book(self, book, rating=None):
        self.books['book'] = rating
        return self.books

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

        for k,v in self.books:
            count +=1
            _sum += self.books[k]
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
        print("The book " + str(self.isbn) + " has been updated.")

    def add_rating(self, rating):
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

    def create_book(self, title, isbn):
        bk = Book(title,isbn)
        return bk

    def create_novel( self, title, author, isbn):
        fictbk = Fiction(title, isbn)
        return fictbk

    def create_non_fiction(self, title, subject, level, isbn):
        nonFictionBook = Non_Fiction(title, subject)
        return nonFictionBook

    def add_book_to_user(self, book, email, rating=None):
        for item in self.users:
            if email in item:
                User.read.read_book(item, rating)
                Book.add_rating(rating)
            if book in self.books:
                self.books['book']= 1
            else:
                self.books['book'] +=1

    def add_user(self, name, email, user_books=None):
        newuser ={}
        newuser['name',email] = User(name, email)

        if user_books:
            for bk in user_books:
                newuser['book'] = self.add_book_to_user(user_books, email)

    def print_catalog(self):
        for k, v in self.books:
            print(v)

    def print_users(self):
        for k,v in self.users:
            print(v)

    def most_read_book(self):
        v=list(self.books.values())
        k=list(self.books.keys())
        return k[v.index(max(v))]

    def highest_rated_book(self):
        v = list(Book.get_average_rating().values())
        k = list(Book.get_average_rating().keys())
        return k[v.index(max(v))]

    def most_positive_user(self):
        v = list(User.get_average_rating().values())
        k = list(User.get_average_rating().keys())
        return k[v.index(max(v))]

    def __repr__(self):
        return str(self.users) + ' a ' + str(self.books)


#Create some books:
Tome_Rater  = Tome_Rater()


#Create some books:
book1 = Tome_Rater.create_book("Society of Mind", 12345678)
novel1 = Tome_Rater.create_novel("Alice In Wonderland", "Lewis Carroll", 12345)

novel1.set_isbn(9781536831139)
nonfiction1 = Tome_Rater.create_non_fiction("Automate the Boring Stuff", "Python", "beginner", 1929452)
nonfiction2 = Tome_Rater.create_non_fiction("Computing Machinery and Intelligence", "AI", "advanced", 11111938)
novel2 = Tome_Rater.create_novel("The Diamond Age", "Neal Stephenson", 10101010)
novel3 = Tome_Rater.create_novel("There Will Come Soft Rains", "Ray Bradbury", 10001000)

#Create users:
Tome_Rater.add_user("Alan Turing", "alan@turing.com")
Tome_Rater.add_user("David Marr", "david@computation.org")

#Add a user with three books already read:
Tome_Rater.add_user("Marvin Minsky", "marvin@mit.edu", user_books=[book1, novel1, nonfiction1])


#Add books to a user one by one, with ratings:
Tome_Rater.add_book_to_user(book1, "alan@turing.com", 1)
Tome_Rater.add_book_to_user(novel1, "alan@turing.com", 3)
Tome_Rater.add_book_to_user(nonfiction1, "alan@turing.com", 3)
Tome_Rater.add_book_to_user(nonfiction2, "alan@turing.com", 4)
Tome_Rater.add_book_to_user(novel3, "alan@turing.com", 1)

Tome_Rater.add_book_to_user(novel2, "marvin@mit.edu", 2)
Tome_Rater.add_book_to_user(novel3, "marvin@mit.edu", 2)
Tome_Rater.add_book_to_user(novel3, "david@computation.org", 4)



#Uncomment these to test your functions:
Tome_Rater.print_catalog()
Tome_Rater.print_users()

print("Most positive user:")
print(Tome_Rater.most_positive_user)
print("Highest rated book:")
print(Tome_Rater.highest_rated_book)
print("Most read book:")
print(Tome_Rater.most_read_book)