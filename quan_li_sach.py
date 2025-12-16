def delete_book():
    show_books()
    if not books:
        return
    try:
        stt = int(input("Nhập số thứ tự sách cần xóa: "))
        books.pop(stt - 1)
        print("✔ Đã xóa sách\n")
    except:
        print("❌ Lỗi! Nhập sai số.\n")