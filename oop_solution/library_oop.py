class Book:
    def __init__(self, id, title, author, total_copies):
        self.id = id
        self.title = title
        self.author = author
        self.total_copies = total_copies
        self.available_copies = total_copies

    def borrow_copy(self):
        if self.available_copies > 0:
            self.available_copies -= 1
            return True
        return False

    def return_copy(self):
        if self.available_copies < self.total_copies:
            self.available_copies += 1
            return True
        return False


class Member:
    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email
        self.borrowed_books = []  

    def borrow_book(self, book):
        if book.borrow_copy():
            self.borrowed_books.append(book.id)
            return True
        return False

    def return_book(self, book):
        if book.id in self.borrowed_books:
            book.return_copy()
            self.borrowed_books.remove(book.id)
            return True
        return False
    

class Library:
    def __init__(self):
        self.books = {}     
        self.members = {}   

    def add_book(self, book):
        self.books[book.id] = book

    def add_member(self, member):
        self.members[member.id] = member

    def borrow_book(self, member_id, book_id):
        if member_id not in self.members:
            return False
        if book_id not in self.books:
            return False

        member = self.members[member_id]
        book = self.books[book_id]

        return member.borrow_book(book)

    def return_book(self, member_id, book_id):
        if member_id not in self.members:
            return False
        if book_id not in self.books:
            return False

        member = self.members[member_id]
        book = self.books[book_id]

        return member.return_book(book)

    def display_books(self):
        return [(b.id, b.title, b.available_copies) for b in self.books.values()]

    def display_members(self):
        return [(m.id, m.name, len(m.borrowed_books)) for m in self.members.values()]
