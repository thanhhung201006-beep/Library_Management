from data import books, borrows

def member_menu(user):
    while True:
        print("\n--- MEMBER ---")
        print("1. Xem sach")
        print("2. Muon sach")
        print("3. Tra sach")
        print("4. Gia han sach")
        print("5. Lich su muon")
        print("6.Danh sach tien phat")
        print("0. Thoat")
        c = input("Chon: ")

        if c == "1":
            for b in books:
                print(b["id"], b["title"], "-", b["status"])

        elif c == "2":
            bid = int(input("Nhap ID sach: "))
            for b in books:
                if b["id"] == bid and b["status"] == "available":
                    b["status"] = "pending"
                    borrows.append({"user":user["username"],"book_id":bid,"due":7,"status":"Chua tra"})

                    print("Yeu cau muon da gui!")
                    break

        elif c == "3":
            bid = int(input("Nhap ID sach tra: "))
            for br in borrows:
                if br["user"]==user["username"] and br["book_id"]==bid:
                    br["status"] = "Da tra"
                    print("Da tra sach!")
                    break

        elif c == "4":
            bid = int(input("Nhap ID sach gia han: "))
            for br in borrows:
                if br["user"]==user["username"] and br["book_id"]==bid:
                    br["due"] += 3
                    print("Gia han them 3 ngay!")

        elif c == "5":
            for br in borrows:
                if br["user"] == user["username"]:
                    print(br)
        elif c == "6":
            from data import fines
            print("Danh sach tien phat:")
            for f in fines:
                if f["user"] == user["username"]:
                    print(f"Sach ID {f['book_id']} - So tien: {f['amount']} VND")
        elif c == "0":
            break
