from data import books
from auth import register

def visitor_menu():
    while True:
        print("\n--- VISITOR ---")
        print("1. Xem sach")
        print("2. Tim sach")
        print("3. Dang ky")
        print("0. Thoat")
        c = input("Chon: ")

        if c == "1":
            for b in books:
                print(b["id"], b["title"], "-", b["author"], "-", b["status"])
        elif c == "2":
            key = input("Nhap tu khoa: ").lower()
            for b in books:
                if key in b["title"].lower() or key in b["author"].lower():
                    print(b["title"], "-", b["author"])
        elif c == "3":
            register()
        elif c == "0":
            break
