from data import users

def login():
    username = input("Nhap username: ")
    password = input("Nhap password: ")

    for u in users:
        if u["username"] == username:
            if u["password"] == password:
                print("Dang nhap thanh cong!")
                return u
            else:
                print("Sai mat khau!")
                return None

    print("Tai khoan khong ton tai!")
    return None


def register():
    print("\n--- DANG KY TAI KHOAN ---")
    username = input("Nhap username: ")

    for u in users:
        if u["username"] == username:
            print("Username da ton tai!")
            return None

    password = input("Nhap password: ")
    users.append({"username": username, "password": password, "role": "member"})
    print("Dang ky thanh cong! Ban co the dang nhap ngay.")
    return True
