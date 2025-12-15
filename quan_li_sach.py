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




