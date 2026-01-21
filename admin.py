from data import users

def admin_menu():
    while True:
        print("\n--- ADMIN ---")
        print("1. Xem user")
        print("2. Xoa user")
        print("0. Thoat")
        c = input("Chon: ")

        if c == "1":
            for u in users:
                print(u["username"], "-", u["role"])
        elif c == "2":
            name = input("Nhap username can xoa: ")
            users[:] = [u for u in users if u["username"] != name]
            print("Da xoa user!")
        elif c == "0":
            break
