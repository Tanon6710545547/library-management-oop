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