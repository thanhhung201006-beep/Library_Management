# --- QUẢN LÝ NGƯỜI DÙNG ---
users = [
    {"username":"admin","password":"123","role":"admin"},
    {"username":"lib","password":"123","role":"librarian"},
    {"username":"lib2","password":"123","role":"librarian"},
    {"username":"mem","password":"123","role":"member"},
    {"username":"mem2","password":"123","role":"member"},
    {"username":"mem3","password":"123","role":"member"}
]

# --- KHO SÁCH ---
books = [
    {"id":1,"title":"Python Basic","author":"Nguyen Van A","year":2020,"status":"available"},
    {"id":2,"title":"Python Advanced","author":"Nguyen Van A","year":2021,"status":"available"},
    {"id":3,"title":"C++ Basic","author":"Tran Van B","year":2019,"status":"available"},
    {"id":4,"title":"C++ Advanced","author":"Tran Van B","year":2022,"status":"available"},
    {"id":5,"title":"Java Core","author":"Le Thi C","year":2018,"status":"available"},
    {"id":6,"title":"Java Spring","author":"Le Thi C","year":2021,"status":"available"},
    {"id":7,"title":"Database System","author":"Pham D","year":2017,"status":"available"},
    {"id":8,"title":"Software Engineering","author":"Nguyen E","year":2019,"status":"available"},
    {"id":9,"title":"AI Fundamentals","author":"Tran F","year":2023,"status":"available"},
    {"id":10,"title":"Machine Learning","author":"Tran F","year":2024,"status":"available"}
]

# --- GIAO DỊCH MƯỢN TRẢ --- 
# Khởi tạo danh sách trống hoặc để dữ liệu mẫu tùy bạn
borrows = [
    {"user": "mem", "book_id": 3, "due": 7, "status": "Chua tra"},
    {"user": "mem2", "book_id": 5, "due": 7, "status": "Da tra"},
    {"user": "mem3", "book_id": 1, "due": 10, "status": "Chua tra"}
]

# --- QUẢN LÝ TIỀN PHẠT ---
fines = [
    {"user":"mem2","book_id":5,"amount":5000}
]