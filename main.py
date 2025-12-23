from quan_li_sach import menu_quan_li_sach
from quan_li_ban_doc import menu_quan_li_ban_doc
from quan_li_muon_tra import menu_muon_tra
from thongkebaocao import menu_thong_ke
from tinh_nang_he_thong import menu_he_thong
from tinhnangtienich import menu_tien_ich
def menu_chinh():
    print("\n===== HỆ THỐNG QUẢN LÍ THƯ VIỆN =====")
    print("1. Quản lí sách")
    print("2. Quản lí bạn đọc")
    print("3. Quản lí mượn trả")
    print("4. Thống kê - báo cáo")
    print("5. Tính năng hệ thống")
    print("6. Tính năng tiện ích")
    print("0. Thoát")
def main():
    while True:
        menu_chinh()
        chon = input("Chọn chức năng: ")

        if chon == "1":
            menu_quan_li_sach()
        elif chon == "2":
            menu_quan_li_ban_doc()
        elif chon == "3":
            menu_muon_tra()
        elif chon == "4":
            menu_thong_ke()
        elif chon == "5":
            menu_he_thong()
        elif chon == "6":
            menu_tien_ich()
        elif chon == "0":
            print("Thoát chương trình.")
            break
        else:
            print("❌ Lựa chọn không hợp lệ!")
if __name__ == "__main__":
    main()