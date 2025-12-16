import json
import shutil
import os
from datetime import datetime

# CẤU HÌNH HỆ THỐNG (DỮ LIỆU ĐÃ CÓ SẴN)

DATA_FILE = "library_data.json"      # Dữ liệu thư viện có sẵn
BACKUP_DIR = "backups"               # Thư mục sao lưu
LOG_FILE = "data_activity.log"       # Nhật ký hoạt động dữ liệu

# NHẬT KÝ HOẠT ĐỘNG DỮ LIỆU

def log_data_activity(action, detail=""):
    """Ghi nhật ký hoạt động liên quan đến dữ liệu"""
    time_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"[{time_str}] {action} | {detail}\n")

# KIỂM TRA DỮ LIỆU CÓ SẴN

def check_existing_data():
    if not os.path.exists(DATA_FILE):
        print("❌ Không tìm thấy dữ liệu thư viện có sẵn")
        return False
    log_data_activity("CHECK", "Kiểm tra dữ liệu thư viện có sẵn")
    return True

# SAO LƯU DỮ LIỆU

def backup_data():
    if not check_existing_data():
        return

    os.makedirs(BACKUP_DIR, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_file = os.path.join(BACKUP_DIR, f"library_backup_{timestamp}.json")

    shutil.copy(DATA_FILE, backup_file)
    log_data_activity("BACKUP", f"Sao lưu dữ liệu vào {backup_file}")
    print("Sao lưu dữ liệu thành công")



