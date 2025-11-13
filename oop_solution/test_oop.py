from library_oop import Book, Member, Library

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

