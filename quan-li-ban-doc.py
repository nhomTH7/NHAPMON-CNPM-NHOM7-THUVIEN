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
