from data import books, borrows # Gọi dữ liệu từ file data

def librarian_menu():
    while True:
        print("\n--- MENU THU THU (LIBRARIAN) ---")
        print("1. Them sach moi vao kho")
        print("2. Duyet yeu cau muon sach")
        print("0. Dang xuat")
        c = input("Chon chuc nang: ") # Giữ phong cách biến 'c' đơn giản của bạn

        if c == "1":
            # Chức năng thêm sách mới
            t = input("Ten sach: ")
            a = input("Tac gia: ")
            y = int(input("Nam xuat ban: "))
            # Tự động tăng ID dựa trên độ dài danh sách hiện tại
            books.append({
                "id": len(books) + 1, 
                "title": t, 
                "author": a, 
                "year": y, 
                "status": "available"
            })
            print("Them sach moi thanh cong!")

        elif c == "2":
            # Hiển thị các yêu cầu mượn đang ở trạng thái 'Cho duyet'
            print("\n--- CAC YEU CAU DANG CHO DUYET ---")
            has_pending = False
            for br in borrows:
                if br["status"] == "Cho duyet":
                    print(f"Thanh vien: {br['user']} | Muon sach ID: {br['book_id']}")
                    has_pending = True
            
            if not has_pending:
                print("Khong co yeu cau nao can xu ly.")
                continue

            # Cho phép nhập nhiều ID cách nhau bằng dấu phẩy (thừa hưởng từ code gốc của bạn)
            ids = input("\nNhap ID các sach muon duyet (vd: 1,3,5): ")
            if ids.strip():
                # Xử lý chuỗi nhập vào thành danh sách số nguyên
                id_list = [int(x.strip()) for x in ids.split(",") if x.strip().isdigit()]

                for bid in id_list:
                    found = False
                    for br in borrows:
                        # Kiểm tra đúng ID và đúng trạng thái đang chờ
                        if br["book_id"] == bid and br["status"] == "Cho duyet":
                            br["status"] = "Da duyet" # Cập nhật trạng thái giao dịch
                            
                            # Cập nhật trạng thái trong kho sách
                            for b in books:
                                if b["id"] == bid:
                                    b["status"] = "borrowed"
                            
                            print(f"-> Da duyet thanh cong sach ID: {bid}")
                            found = True
                            break
                    
                    if not found:
                        print(f"-> Khong tim thay yeu cau cho sach ID {bid} hoac ID khong hop le.")

        elif c == "0":
            break