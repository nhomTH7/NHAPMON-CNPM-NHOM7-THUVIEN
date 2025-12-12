nha_san_xuat = {
    "NSX01": {
        "ten_nsx": "NXB Kim Đồng",
        "thoigian_xuatban": "2020",
        "so_sach_trong_thuvien": 120
    }
}

def cap_nhat_thong_tin_nsx(ma_nsx):
    if ma_nsx not in nha_san_xuat:
        print("❌ Nhà sản xuất không tồn tại!")
        return
    
    nsx = nha_san_xuat[ma_nsx]

    print("\n===== CẬP NHẬT THÔNG TIN NHÀ SẢN XUẤT =====")
    #1. CẬP NHẬT TÊN NHÀ SẢN XUẤT
    ten_moi = input(f"Nhập tên nhà sản xuất mới (hiện tại: {nsx['ten_nsx']}): ")
    if ten_moi.strip() != "":
        nsx["ten_nsx"] = ten_moi
    #2. CẬP NHẬT THỜI GIAN XUẤT BẢN
    tg_moi = input(f"Nhập thời gian được xuất bản (hiện tại: {nsx['thoigian_xuatban']}): ")
    if tg_moi.strip() != "":
        nsx["thoigian_xuatban"] = tg_moi
         # 3️⃣ CẬP NHẬT SỐ SÁCH CÓ TRONG THƯ VIỆN
    so_sach_moi = input(f"Nhập số sách trong thư viện (hiện tại: {nsx['so_sach_trong_thuvien']}): ")
    if so_sach_moi.strip() != "":
        nsx["so_sach_trong_thuvien"] = int(so_sach_moi)

    print("\n✅ CẬP NHẬT THÀNH CÔNG!")
    print("Thông tin sau khi cập nhật:", nsx)
