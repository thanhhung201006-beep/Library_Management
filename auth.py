from data import users

def login():
    u = input("Username: ")
    p = input("Password: ")
    for user in users:
        if user["username"] == u and user["password"] == p:
            return user
    print("Sai tai khoan!")
    return None

def register():
    u = input("Nhap username: ")
    p = input("Nhap password: ")
    users.append({"username":u,"password":p,"role":"member"})
    print("Dang ky thanh cong! Ban la MEMBER.")
