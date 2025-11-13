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


