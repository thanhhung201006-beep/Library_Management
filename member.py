from data import books, borrows, fines # Đưa tất cả các bảng dữ liệu lên đầu file

def member_menu(user):
    while True:
        print(f"\n--- MENU THANH VIEN: {user['username'].upper()} ---") # Hiển thị tên user cho chuyên nghiệp
        print("1. Xem danh sach sach")
        print("2. Dang ky muon sach")
        print("3. Tra sach")
        print("4. Gia han sach")
        print("5. Lich su muon")
        print("6. Danh sach tien phat")
        print("0. Dang xuat")
        c = input("Chon chuc nang: ") # Sử dụng biến 'c' đơn giản theo phong cách của bạn

        if c == "1":
            # Hiển thị danh sách sách kèm trạng thái hiện tại
            for b in books:
                print(f"ID: {b['id']} - {b['title']} | Trang thai: {b['status']}")

        elif c == "2":
            bid = int(input("Nhap ID sach muon: "))
            for b in books:
                # Chỉ cho phép mượn nếu sách đang ở trạng thái 'available'
                if b["id"] == bid:
                    if b["status"] == "available":
                        b["status"] = "pending" # Chuyển sang chờ duyệt để Thu thư xử lý
                        borrows.append({
                            "user": user["username"], 
                            "book_id": bid, 
                            "due": 7, 
                            "status": "Cho duyet"
                        })
                        print("Yeu cau muon da gui den Thu thu!")
                    else:
                        print("Sach hien khong co san de muon.")
                    break

        elif c == "3":
            bid = int(input("Nhap ID sach muon tra: "))
            found = False
            for br in borrows:
                # Chỉ cho trả những sách đã được duyệt mượn
                if br["user"] == user["username"] and br["book_id"] == bid and br["status"] == "Da duyet":
                    br["status"] = "Da tra"
                    # Cập nhật lại kho sách để người khác có thể mượn
                    for b in books:
                        if b["id"] == bid:
                            b["status"] = "available"
                    print("Tra sach thanh cong!")
                    found = True
                    break
            if not found:
                print("Khong tim thay giao dich mượn phù hợp để trả.")

        elif c == "4":
            bid = int(input("Nhap ID sach muon gia han: "))
            for br in borrows:
                if br["user"] == user["username"] and br["book_id"] == bid and br["status"] == "Da duyet":
                    br["due"] += 3 # Tăng thời gian mượn thêm 3 ngày
                    print("Gia han thanh cong them 3 ngay!")
                    break

        elif c == "5":
            print("--- LICH SU GIAO DICH ---")
            for br in borrows:
                if br["user"] == user["username"]:
                    print(f"Sach ID: {br['book_id']} | Ngay thue: {br['due']} ngay | Trang thai: {br['status']}")

        elif c == "6":
            print("--- DANH SACH TIEN PHAT ---")
            for f in fines:
                if f["user"] == user["username"]:
                    print(f"Sach ID: {f['book_id']} - So tien: {f['amount']} VND")

        elif c == "0":
            break