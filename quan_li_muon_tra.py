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

     # Công việc: Trả sách
    elif chon == "2":
        ten = input("Nhập tên người trả sách: ")
        tim_thay = False

        for record in ds_muon_tra:
            if record["ten"] == ten and record["ngay_tra"] is None:
                ngay_tra = input("Nhập ngày trả (dd/mm/yyyy): ")
                record["ngay_tra"] = ngay_tra
                tim_thay = True

                han_tra = datetime.strptime(record["han_tra"], "%d/%m/%Y")
                ngay_tra_dt = datetime.strptime(ngay_tra, "%d/%m/%Y")

                if ngay_tra_dt < han_tra:
                    print("📗 Trả sách TRƯỚC hạn")
                elif ngay_tra_dt == han_tra:
                    print("📘 Trả sách ĐÚNG hạn")
                else:
                    print("📕 Trả sách QUÁ hạn")

                print("✅ Trả sách thành công!")