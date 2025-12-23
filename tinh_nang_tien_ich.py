from qr_scanner import scan_qr
from book_suggest import suggest_books

def menu():
    print("\n====== TÍNH NĂNG TIỆN ÍCH ======")
    print("1. Quét mã QR sách")
    print("2. Quét mã QR thẻ bạn đọc")
    print("3. Gợi ý sách cùng thể loại")
    print("0. Thoát")
    
while True:
    menu()
    choice = input("👉 Chọn chức năng: ")
if choice == "1":
        print("\n📖 Quét mã QR sách")
        book_code = scan_qr("Quet QR Sach")
        if book_code:
            print("✅ Mã sách:", book_code)
elif choice == "2":
        print("\n🪪 Quét mã QR thẻ bạn đọc")
        reader_code = scan_qr("Quet QR Ban Doc")
        if reader_code:
            print("✅ Mã bạn đọc:", reader_code)
        elif choice == "3":
         print("\n🔍 Gợi ý sách cùng thể loại")
        print("Các thể loại: CNTT | KHOAHOC | VANHOC")
        category = input("Nhập thể loại: ")

        books = suggest_books(category)
        if books:
            print("📚 Sách gợi ý:")
            for book in books:
                print("- ", book)
        else:
            print("❌ Không tìm thấy thể loại!")

elif choice == "0":
         print("👋 Thoát chương trình")
         break

else:
 feature/quan_li_thu_vien
        print("❌ Lựa chọn không hợp lệ!")
=======
        print("❌ Lựa chọn không hợp lệ!")
 main
