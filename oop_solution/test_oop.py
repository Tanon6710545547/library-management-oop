from library_oop import Book

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
