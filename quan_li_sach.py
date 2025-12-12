
# Danh sách lưu sách
books = []
def add_book():
    title = input("Nhập tên sách: ")
    author = input("Nhập tác giả: ")
    book = {"title": title, "author": author}
    books.append(book)
    print("✔ Đã thêm sách\n")
# ============================
# CHƯƠNG TRÌNH QUẢN LÝ SÁCH
# ============================

# Mỗi quyển sách là 1 dict:
# { "id": ..., "ten": ..., "tac_gia": ..., "nam": ..., "so_luong": ... }

danh_sach_sach = [] 
