from datetime import datetime

# ============================
# Khởi tạo danh sách mượn trả
# ============================
ds_muon_tra = []

while True:
    print("\n===== QUẢN LÍ MƯỢN TRẢ SÁCH =====")
    print("1. Mượn sách")
    print("2. Trả sách")
    print("3. Thống kê trong ngày")
    print("0. Thoát")

    chon = input("Chọn chức năng: ")

     # Công việc: Mượn sách
    if chon == "1":
        ten = input("Nhập tên người mượn: ")
        sach = input("Nhập tên sách: ")
        ngay_muon = input("Nhập ngày mượn (dd/mm/yyyy): ")
        han_tra = input("Nhập hạn trả (dd/mm/yyyy): ")

        ds_muon_tra.append({
            "ten": ten,
            "sach": sach,
            "ngay_muon": ngay_muon,
            "han_tra": han_tra,
            "ngay_tra": None
        })

        print("✅ Mượn sách thành công!")