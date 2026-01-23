from data import books, borrows, CURRENT_DAY, FINE_PER_DAY

def member_menu(user):
    while True:
        print("\n--- MEMBER MENU ---")
        print("1. Xem danh sach sach")
        print("2. Muon sach")
        print("3. Tra sach")
        print("4. Xem lich su muon")
        print("5. Xem tien phat")
        print("0. Dang xuat")

        choice = input("Chon: ")

        if not choice.isdigit():
            print("Lua chon khong hop le!")
            continue

        if choice == "1":
            for b in books:
                print(b)

        elif choice == "2":
            borrow_book(user)

        elif choice == "3":
            return_book(user)

        elif choice == "4":
            view_history(user)

        elif choice == "5":
            view_fine(user)

        elif choice == "0":
            break

        else:
            print("Lua chon khong hop le!")

def borrow_book(user):
    bid_input = input("Nhap ID sach: ")

    if not bid_input.isdigit():
        print("ID sach phai la so!")
        return

    bid = int(bid_input)

    book = None
    for b in books:
        if b["id"] == bid:
            book = b

    if not book:
        print("Khong tim thay sach!")
        return

    if book["status"] != "available":
        print("Sach da duoc muon!")
        return

    borrows.append({
        "user": user["username"],
        "book_id": bid,
        "borrow_day": CURRENT_DAY,
        "due": 7,
        "status": "Chua tra",
        "fine": 0
    })
    book["status"] = "pending"
    print("Yeu cau muon sach da duoc gui!")

def return_book(user):
    bid_input = input("Nhap ID sach can tra: ")

    if not bid_input.isdigit():
        print("ID sach phai la so!")
        return

    bid = int(bid_input)

    found = False
    for br in borrows:
        if br["user"] == user["username"] and br["book_id"] == bid and br["status"] == "Chua tra":
            days_late = CURRENT_DAY - (br["borrow_day"] + br["due"])
            if days_late > 0:
                br["fine"] = days_late * FINE_PER_DAY
                print(f"Ban tra tre {days_late} ngay.")
                print(f"Tien phat: {br['fine']} VND")
            else:
                print("Tra dung han. Khong bi phat.")

            br["status"] = "Da tra"
            for b in books:
                if b["id"] == bid:
                    b["status"] = "available"

            print("Tra sach thanh cong!")
            found = True

    if not found:
        print("Ban chua muon sach nay!")

def view_history(user):
    print("\n--- LICH SU MUON ---")
    for br in borrows:
        if br["user"] == user["username"]:
            print(f"Sach ID {br['book_id']} | Trang thai: {br['status']} | Tien phat: {br['fine']} VND")

def view_fine(user):
    total = 0
    print("\n--- TIEN PHAT CUA BAN ---")
    for br in borrows:
        if br["user"] == user["username"] and br["fine"] > 0:
            print(f"Sach ID {br['book_id']} - Tien phat: {br['fine']} VND")
            total += br["fine"]

    if total == 0:
        print("Ban khong co tien phat nao.")
    else:
        print(f"TONG TIEN PHAT: {total} VND")
