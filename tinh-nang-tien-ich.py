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
