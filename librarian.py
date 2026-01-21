from data import books, borrows

def librarian_menu():
    while True:
        print("\n--- LIBRARIAN ---")
        print("1. Them sach")
        print("2. Duyet muon sach")
        print("0. Thoat")
        c = input("Chon: ")

        if c == "1":
            t = input("Ten sach: ")
            a = input("Tac gia: ")
            y = int(input("Nam: "))
            books.append({"id":len(books)+1,"title":t,"author":a,"year":y,"status":"available"})
            print("Them sach thanh cong!")


        elif c == "2":

            print("Danh sach sach dang cho duyet:")

            for br in borrows:

                if br["status"] == "Chua tra":
                    print(br)

            ids = input("Nhap ID sach can duyet (vd: 1,3,5): ")

            id_list = [int(x.strip()) for x in ids.split(",")]

            for bid in id_list:

                found = False

                for br in borrows:

                    if br["book_id"] == bid and br["status"] == "Chua tra":

                        for b in books:

                            if b["id"] == bid:
                                b["status"] = "borrowed"

                                print(f"Da duyet sach ID {bid}")

                                found = True

                if not found:
                    print(f"Khong tim thay sach ID {bid} hoac da duoc xu ly!")


        elif c == "0":
            break
