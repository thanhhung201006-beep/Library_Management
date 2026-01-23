from auth import login, register
from visitor import visitor_menu
from member import member_menu
from librarian import librarian_menu
from admin import admin_menu

def main():
    while True:
        print("\n--- HE THONG QUAN LY THU VIEN ---")
        print("1. Dang nhap")
        print("2. Dang ky tai khoan")
        print("3. Visitor")
        print("0. Thoat")

        choice = input("Chon: ")

        if not choice.isdigit():
            print("Lua chon khong hop le!")
            continue

        if choice == "1":
            user = login()
            if user:
                if user["role"] == "member":
                    member_menu(user)
                elif user["role"] == "librarian":
                    librarian_menu()
                elif user["role"] == "admin":
                    admin_menu()

        elif choice == "2":
            register()

        elif choice == "3":
            visitor_menu()

        elif choice == "0":
            print("Tam biet!")
            break

        else:
            print("Lua chon khong hop le!")

if __name__ == "__main__":
    main()
