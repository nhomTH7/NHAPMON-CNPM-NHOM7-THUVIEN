2. Cập nhật thông tin sách
# ----------------------------
def cap_nhat_sach():
    print("\n=== CẬP NHẬT SÁCH ===")
    id = input("Nhập mã sách cần cập nhật: ")

    for sach in danh_sach_sach:
        if sach["id"] == id:
            print("Tìm thấy sách:", sach["ten"])
            sach["ten"] = input("Tên mới: ")
            sach["tac_gia"] = input("Tác giả mới: ")
            sach["nam"] = input("Năm xuất bản mới: ")
            sach["so_luong"] = int(input("Số lượng mới: "))
            print("✔ Cập nhật thành công!")
            return
    
    print("❌ Không tìm thấy sách!")