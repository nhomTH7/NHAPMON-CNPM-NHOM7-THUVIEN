from modules.borrow_day import borrow_book
from modules.return_day import return_book
from modules.count_borrow import count_borrow_in_day
from modules.count_return import count_return_in_day

print("=== Quản lí mượn - trả sách ===")

borrow_book("SV01", "S001", "10/12/2025", "15/12/2025")
return_book("SV01", "S001", "14/12/2025")

count_borrow_in_day("10/12/2025")
count_return_in_day("14/12/2025")

