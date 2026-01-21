from auth import login, register
from visitor import visitor_menu
from member import member_menu
from librarian import librarian_menu
from admin import admin_menu

def main():
    while True:
        print("\n=== LIBRARY MANAGEMENT SYSTEM ===")
        print("1. Dang ky")
        print("2. Login")
        print("3. Visitor")
        print("0. Thoat")
        c = input("Chon: ")

        if c == "1":
            register()
        elif c == "2":
            user = login()
            if user:
                if user["role"] == "member":
                    member_menu(user)
                elif user["role"] == "librarian":
                    librarian_menu()
                elif user["role"] == "admin":
                    admin_menu()
        elif c == "3":
            visitor_menu()
        elif c == "0":
            break

main()
