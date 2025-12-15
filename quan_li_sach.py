# ============================
# CHƯƠNG TRÌNH QUẢN LÝ SÁCH
# ============================

# Mỗi quyển sách là 1 dict:
# { "id": ..., "ten": ..., "tac_gia": ..., "nam": ..., "so_luong": ... }

danh_sach_sach = [] 
# Danh sách lưu sách
books = []
def add_book():
    title = input("Nhập tên sách: ")
    author = input("Nhập tác giả: ")
    book = {"title": title, "author": author}
    books.append(book)
    print("✔ Đã thêm sách\n")


def show_books():
    if not books:
        print("Không có sách nào.\n")
        return
    print("\nDanh sách sách:")
    for i, b in enumerate(books, start=1):
        print(f"{i}. {b['title']} - {b['author']}")
    print()
def delete_book():
    show_books()
    if not books:
        return
    try:
        index = int(input("Nhập số thứ tự sách muốn xóa: "))
        books.pop(index - 1)
        print("✔ Đã xóa sách\n")
    except:
        print("❌ Số không hợp lệ.\n")
def main():
    while True:
        print("=== QUẢN LÝ SÁCH ===")
        print("1. Thêm sách")
        print("2. Hiển thị sách")
        print("3. Xóa sách")
        print("0. Thoát")
        choice = input("Chọn: ")

        if choice == "1":
            add_book()
        elif choice == "2":
            show_books()
        elif choice == "3":
            delete_book()
        elif choice == "0":
            print("Tạm biệt!")
            break
        else:
            print("Lựa chọn không hợp lệ.\n")

if __name__ == "__main__":
    main()
