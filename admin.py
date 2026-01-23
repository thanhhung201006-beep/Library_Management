from data import users

def admin_menu():
    while True:
        print("\n--- ADMIN MENU ---")
        print("1. Xem danh sach user")
        print("2. Xoa user")
        print("0. Dang xuat")

        choice = input("Chon: ")

        if not choice.isdigit():
            print("Lua chon khong hop le!")
            continue

        if choice == "1":
            for u in users:
                print(u)

        elif choice == "2":
            delete_user()

        elif choice == "0":
            break

        else:
            print("Lua chon khong hop le!")

def delete_user():
    uname = input("Nhap username can xoa: ")

    found = False
    for u in users:
        if u["username"] == uname:
            users.remove(u)
            print("Da xoa tai khoan!")
            found = True
            break

    if not found:
        print("Khong tim thay tai khoan!")
