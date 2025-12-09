# quanlisach.py

books = []

def them_sach():
    print("\n=== THÊM SÁCH MỚI ===")

    ma_sach = input("Mã sách: ")
    ten = input("Tên sách: ")
    tac_gia = input("Tác giả: ")
    nxb = input("Nhà xuất bản: ")
    nam_xb = input("Năm xuất bản: ")
    so_luong = input("Số lượng: ")

    sach = {
        "ma_sach": ma_sach,
        "ten": ten,
        "tac_gia": tac_gia,
        "nxb": nxb,
        "nam_xb": nam_xb,
        "so_luong": so_luong
    }

    books.append(sach)
    print(">> Đã thêm sách thành công!")
