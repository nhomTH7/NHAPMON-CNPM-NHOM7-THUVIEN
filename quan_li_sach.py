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


def search_book():
    key = input("Nhập tên sách cần tra cứu: ").lower()
    for b in books:
        if key in b["ten"].lower():
            print(b["ten"], "-", b["tac_gia"])
    print()