from data import books, borrows

def librarian_menu():
    while True:
        print("\n--- LIBRARIAN MENU ---")
        print("1. Xem danh sach sach")
        print("2. Duyet yeu cau muon")
        print("0. Dang xuat")

        choice = input("Chon: ")

        if not choice.isdigit():
            print("Lua chon khong hop le!")
            continue

        if choice == "1":
            for b in books:
                print(b)

        elif choice == "2":
            approve_borrow()

        elif choice == "0":
            break

        else:
            print("Lua chon khong hop le!")

def approve_borrow():
    print("\n--- DANH SACH CHO DUYET ---")
    pending = False
    for br in borrows:
        if br["status"] == "Chua tra":
            print(br)
            pending = True

    if not pending:
        print("Khong co yeu cau muon nao!")
        return

    bid_input = input("Nhap ID sach can duyet: ")

    if not bid_input.isdigit():
        print("ID sach phai la so!")
        return

    bid = int(bid_input)
    found = False

    for br in borrows:
        if br["book_id"] == bid and br["status"] == "Chua tra":
            for b in books:
                if b["id"] == bid:
                    b["status"] = "borrowed"
                    print("Da duyet muon sach!")
                    found = True

    if not found:
        print("Khong co yeu cau muon cho sach nay!")
