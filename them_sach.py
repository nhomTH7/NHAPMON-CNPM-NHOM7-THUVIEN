1. Thêm sách
# ----------------------------
def them_sach():
    print("\n=== THÊM SÁCH MỚI ===")
    id = input("Nhập mã sách: ")
    ten = input("Tên sách: ")
    tac_gia = input("Tác giả: ")
    nam = input("Năm xuất bản: ")
    so_luong = int(input("Số lượng: "))

    sach = {
        "id": id,
        "ten": ten,
        "tac_gia": tac_gia,
        "nam": nam,
        "so_luong": so_luong
    }

    danh_sach_sach.append(sach)
    print("✔ Thêm sách thành công!")
