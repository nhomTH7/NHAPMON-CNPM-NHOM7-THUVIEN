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
    #CẬP NHẬT TÊN NHÀ SẢN XUẤT
    # ---------------------------------------------------
    ten_moi = input(f"Nhập tên nhà sản xuất mới (hiện tại: {nsx['ten_nsx']}): ")
    if ten_moi.strip() != "":
        nsx["ten_nsx"] = ten_moi
