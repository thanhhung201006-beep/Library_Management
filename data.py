users = [
    {"username": "admin", "password": "123", "role": "admin"},
    {"username": "lib", "password": "123", "role": "librarian"},
    {"username": "mem", "password": "123", "role": "member"}
]

books = [
    {"id": 1, "title": "Python Basic", "status": "available"},
    {"id": 2, "title": "OOP in Python", "status": "available"},
    {"id": 3, "title": "Data Structures", "status": "available"},
    {"id": 4, "title": "Machine Learning", "status": "available"},
    {"id": 5, "title": "AI for Beginner", "status": "available"}
]

borrows = [
    {"user": "mem", "book_id": 3, "borrow_day": 1, "due": 7, "status": "Chua tra", "fine": 0},
    {"user": "mem", "book_id": 5, "borrow_day": 1, "due": 7, "status": "Da tra", "fine": 0}
]

CURRENT_DAY = 10   # giả lập ngày hiện tại
FINE_PER_DAY = 5000
