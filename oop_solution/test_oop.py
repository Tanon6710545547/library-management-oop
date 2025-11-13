from library_oop import Book, Member, Library

def test_create_book():
    b = Book(1, "A", "B", 3)
    assert b.available_copies == 3

def test_borrow_success():
    b = Book(1, "A", "B", 3)
    assert b.borrow_copy() is True
    assert b.available_copies == 2

def test_borrow_fail_no_copies():
    b = Book(1, "A", "B", 1)
    b.borrow_copy()
    assert b.borrow_copy() is False
    assert b.available_copies == 0

def test_return_success():
    b = Book(1, "A", "B", 3)
    b.borrow_copy()
    assert b.return_copy() is True
    assert b.available_copies == 3

def test_return_fail_full():
    b = Book(1, "A", "B", 3)
    assert b.return_copy() is False
    assert b.available_copies == 3

def test_member_borrow_success():
    book = Book(1, "A", "B", 2)
    m = Member(1, "Alice", "a@mail.com")
    assert m.borrow_book(book) is True
    assert 1 in m.borrowed_books
    assert book.available_copies == 1

def test_member_borrow_fail_no_copies():
    book = Book(1, "A", "B", 0)
    m = Member(1, "Alice", "a@mail.com")
    assert m.borrow_book(book) is False
    assert len(m.borrowed_books) == 0

def test_member_return_success():
    book = Book(1, "A", "B", 1)
    m = Member(1, "Alice", "a@mail.com")
    m.borrow_book(book)
    assert m.return_book(book) is True
    assert 1 not in m.borrowed_books
    assert book.available_copies == 1

def test_member_return_fail_not_borrowed():
    book = Book(1, "A", "B", 1)
    m = Member(1, "Alice", "a@mail.com")
    assert m.return_book(book) is False
    assert book.available_copies == 1

def test_library_add_book():
    lib = Library()
    b = Book(1, "A", "B", 3)
    lib.add_book(b)
    assert 1 in lib.books

def test_library_add_member():
    lib = Library()
    m = Member(1, "Alice", "a@mail.com")
    lib.add_member(m)
    assert 1 in lib.members

def test_library_borrow_success():
    lib = Library()
    b = Book(1, "A", "B", 1)
    m = Member(1, "Alice", "a@mail.com")
    lib.add_book(b)
    lib.add_member(m)
    assert lib.borrow_book(1, 1) is True
    assert b.available_copies == 0
    assert 1 in m.borrowed_books

def test_library_borrow_fail_no_member():
    lib = Library()
    b = Book(1, "A", "B", 1)
    lib.add_book(b)
    assert lib.borrow_book(999, 1) is False

def test_library_borrow_fail_no_book():
    lib = Library()
    m = Member(1, "Alice", "a@mail.com")
    lib.add_member(m)
    assert lib.borrow_book(1, 999) is False

def test_library_return_success():
    lib = Library()
    b = Book(1, "A", "B", 1)
    m = Member(1, "Alice", "a@mail.com")
    lib.add_book(b)
    lib.add_member(m)
    lib.borrow_book(1, 1)
    assert lib.return_book(1, 1) is True
    assert b.available_copies == 1
    assert 1 not in m.borrowed_books

def test_library_return_fail_not_borrowed():
    lib = Library()
    b = Book(1, "A", "B", 1)
    m = Member(1, "Alice", "a@mail.com")
    lib.add_book(b)
    lib.add_member(m)
    assert lib.return_book(1, 1) is False

def test_integration_full_flow():
    lib = Library()
    b1 = Book(1, "A", "B", 2)
    b2 = Book(2, "C", "D", 1)
    m1 = Member(1, "Alice", "a@mail.com")
    lib.add_book(b1)
    lib.add_book(b2)
    lib.add_member(m1)
    assert lib.borrow_book(1, 1) is True
    assert lib.borrow_book(1, 2) is True
    assert b1.available_copies == 1
    assert b2.available_copies == 0
    assert m1.borrowed_books == [1, 2]
    assert lib.return_book(1, 1) is True
    assert b1.available_copies == 2
    assert b2.available_copies == 0
    assert m1.borrowed_books == [2]
