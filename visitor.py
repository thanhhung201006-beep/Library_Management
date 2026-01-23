from data import users, books

def visitor_menu():
    while True:
        print("\n--- VISITOR MENU ---")
        print("1. Xem danh sach sach")
        print("2. Dang ky tai khoan")
        print("0. Thoat")

        choice = input("Chon: ")

        if not choice.isdigit():
            print("Lua chon khong hop le!")
            continue

        if choice == "1":
            for b in books:
                print(b)

        elif choice == "2":
            register()

        elif choice == "0":
            break

        else:
            print("Lua chon khong hop le!")

def register():
    username = input("Nhap username: ")

    for u in users:
        if u["username"] == username:
            print("Username da ton tai!")
            return

    password = input("Nhap password: ")
    users.append({"username": username, "password": password, "role": "member"})
    print("Dang ky thanh cong!")
