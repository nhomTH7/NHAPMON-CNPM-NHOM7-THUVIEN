

while True:
    print("\n===== QUẢN LÍ MƯỢN TRẢ SÁCH =====")
    print("1. Mượn sách")
    print("2. Trả sách")
    print("3. Thống kê trong ngày")
    print("4. cập nhật số lượng sách")   
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

        print(" Mượn sách thành công!")

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
                    print(" Trả sách TRƯỚC hạn")
                elif ngay_tra_dt == han_tra:
                    print("Trả sách ĐÚNG hạn")
                else:
                    print(" Trả sách QUÁ hạn")

 feature/quan_li_thu_vien
                print("✅ Trả sách thành công!")
                print("Trả sách thành công!")
                break

        if not tim_thay:

            print("Không tìm thấy thông tin mượn sách!")    
            print("❌ Không tìm thấy thông tin mượn sách!")    
     # Công việc: Thống kê trong ngày
    elif chon == "3":
        hom_nay = datetime.now().strftime("%d/%m/%Y")
        so_luot_muon = 0
        so_luot_tra = 0

        for record in ds_muon_tra:
            if record["ngay_muon"] == hom_nay:
                so_luot_muon += 1
            if record["ngay_tra"] == hom_nay:
                so_luot_tra += 1

        print(f"📊 Thống kê ngày {hom_nay}")
        print(f"📘 Số lượt mượn: {so_luot_muon}")
        print(f"📗 Số lượt trả: {so_luot_tra}")       

        print("❌ Không tìm thấy thông tin mượn sách!")    
            # Công việc: Cập nhật số lượng sách
    elif chon == "4":
        ten_sach = input("Nhập tên sách cần cập nhật: ")

        if ten_sach not in ds_sach:
            print(" Sách không tồn tại!")
        else:
            print(f"Số lượng hiện tại của '{ten_sach}': {ds_sach[ten_sach]}")
            so_luong_moi = int(input("Nhập số lượng mới: "))

            if so_luong_moi < 0:
                print(" Số lượng không hợp lệ!")
            else:
                ds_sach[ten_sach] = so_luong_moi
                print(" Cập nhật số lượng sách thành công!")
            print("❌ Không tìm thấy thông tin mượn sách!")    
 main
