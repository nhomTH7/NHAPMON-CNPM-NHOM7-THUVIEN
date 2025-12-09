# them_sach.py
def them_sach(ds_sach):
    ma = input("Nhập mã sách: ")
    ten = input("Nhập tên sách: ")
    tac_gia = input("Nhập tác giả: ")
    nam = input("Nhập năm xuất bản: ")

    sach = {
        "ma": ma,
        "ten": ten,
        "tac_gia": tac_gia,
        "nam": nam
    }

    ds_sach.append(sach)
    print("\n==> Thêm sách thành công!\n")

# Ví dụ chạy thử
if __name__ == "__main__":
    danh_sach = []
    them_sach(danh_sach)
    print(danh_sach)
