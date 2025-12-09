class LibraryManager:
    def __init__(self):
        self.readers = {}     # lưu dạng dictionary: key = reader_id
        # -----------------------
    # 1. Thêm bạn đọc
    # -----------------------
    def add_reader(self, reader_id, name, email, phone):
        if reader_id in self.readers:
            print("❌ Mã bạn đọc đã tồn tại!")
            return

        new_reader = Reader(reader_id, name, email, phone)
        self.readers[reader_id] = new_reader
        print("✔ Thêm bạn đọc thành công!")
    # 2. Sửa thông tin bạn đọc
    # -----------------------
    def update_reader(self, reader_id, name=None, email=None, phone=None):
        if reader_id not in self.readers:
            print("❌ Không tìm thấy bạn đọc!")
            return
        
        reader = self.readers[reader_id]
        if name: reader.name = name
        if email: reader.email = email
        if phone: reader.phone = phone

        print("✔ Cập nhật thông tin thành công!")
    # 3. Xóa bạn đọc
    # -----------------------
    def delete_reader(self, reader_id):
        if reader_id in self.readers:
            del self.readers[reader_id]
            print("✔ Xóa bạn đọc thành công!")
        else:
            print("❌ Không tìm thấy mã bạn đọc!")
    # 4. Tìm kiếm bạn đọc
    # -----------------------
    def search_reader(self, keyword):
        print("🔎 Kết quả tìm kiếm:")
        found = False
        for reader in self.readers.values():
            if keyword.lower() in reader.name.lower() or keyword in reader.reader_id:
                print(reader)
                found = True
        
        if not found:
            print("❌ Không tìm thấy bạn đọc!")
    # 5. Xem lịch sử mượn trả
    # -----------------------
    def view_history(self, reader_id):
        if reader_id not in self.readers:
            print("❌ Không tìm thấy bạn đọc!")
            return
        
        reader = self.readers[reader_id]

        print(f"📘 Lịch sử mượn trả của {reader.name}:")
        if not reader.borrow_history:
            print("Không có dữ liệu!")
        else:
            for item in reader.borrow_history:
                print(f"- {item}")