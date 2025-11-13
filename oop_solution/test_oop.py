from library_oop import Book, Member

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

