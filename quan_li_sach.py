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
  