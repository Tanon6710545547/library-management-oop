# Library Management OOP

## Project Overview
This project converts a procedural library management program into an Object-Oriented version. The system manages books, members, and borrowing operations.

## Project Structure
- procedural_version/
  - library_procedural.py
  - test_procedural.py
- oop_solution/
  - library_oop.py
  - test_oop.py

## Design Overview
### Book
- Stores book information.
- Tracks total and available copies.
- Supports borrow and return actions.

### Member
- Stores member information.
- Tracks borrowed book IDs.
- Supports borrow and return actions through Book objects.

### Library
- Manages all books and members.
- Provides add, borrow, and return operations.

## Testing
The test file (test_oop.py) includes:
- Book tests
- Member tests
- Library tests
- Integration test combining all classes

Run tests using:
