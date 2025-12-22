import sqlite3
from tabulate import tabulate

# Kết nối database
conn = sqlite3.connect("library.db")
cursor = conn.cursor()


def report_most_borrowed_books():
    query = """
        SELECT s.MaSach, s.TenSach, COUNT(mt.MaSach) AS SoLanMuon
        FROM MuonTra mt
        JOIN Sach s ON mt.MaSach = s.MaSach
        GROUP BY s.MaSach, s.TenSach
        ORDER BY SoLanMuon DESC
        LIMIT 10;
    """
    cursor.execute(query)
    result = cursor.fetchall()
    print("\n📌 Báo cáo sách được mượn nhiều nhất:")
    print(tabulate(result, headers=["Mã sách", "Tên sách", "Số lần mượn"], tablefmt="github"))
def report_damaged_lost_books():
    query = """
        SELECT s.MaSach, s.TenSach,
               SUM(CASE WHEN mt.TinhTrangTra = 'Hong' THEN 1 ELSE 0 END) AS SoLuongHong,
               SUM(CASE WHEN mt.TinhTrangTra = 'Mat' THEN 1 ELSE 0 END) AS SoLuongMat
        FROM MuonTra mt
        JOIN Sach s ON mt.MaSach = s.MaSach
        GROUP BY s.MaSach, s.TenSach;
    """
    cursor.execute(query)
    result = cursor.fetchall()
    print("\n Báo cáo sách hỏng/mất:")
    print(tabulate(result, headers=["Mã sách", "Tên sách", "Hỏng", "Mất"], tablefmt="github"))
    
    #báo cáo bạn đọc mượn nhiều nhất
    def report_top_readers():
    query = """
        SELECT bd.MaBanDoc, bd.HoTen, COUNT(mt.MaBanDoc) AS SoLanMuon
        FROM MuonTra mt
        JOIN BanDoc bd ON mt.MaBanDoc = bd.MaBanDoc
        GROUP BY bd.MaBanDoc, bd.HoTen
        ORDER BY SoLanMuon DESC
        LIMIT 10;
    """
    cursor.execute(query)
    result = cursor.fetchall()
    print("\n Báo cáo bạn đọc mượn nhiều nhất:")
    print(tabulate(result, headers=["Mã bạn đọc", "Họ tên", "Số lần mượn"], tablefmt="github"))
 
def report_damaged_assets():
    query = """
        SELECT MaTaiSan, TenTaiSan, SoLuongHuHong, NgayPhatHien, GhiChu
        FROM TaiSanHuHong
        ORDER BY NgayPhatHien DESC;
    """
    cursor.execute(query)
    result = cursor.fetchall()
    print("\n Báo cáo tài sản hư hỏng:")
    print(tabulate(result, headers=["Mã tài sản", "Tên tài sản", "SL Hư hỏng", "Ngày phát hiện", "Ghi chú"], tablefmt="github"))
    def report_books_per_category():
    query = """
        SELECT tl.MaTheLoai, tl.TenTheLoai,
               COUNT(s.MaSach) AS SoLuongSach
        FROM Sach s
        JOIN TheLoai tl ON s.MaTheLoai = tl.MaTheLoai
        GROUP BY tl.MaTheLoai, tl.TenTheLoai
        ORDER BY SoLuongSach DESC;
    """
    cursor.execute(query)
    result = cursor.fetchall()
    print("\n📌 Thống kê số lượng sách theo thể loại:")
    print(tabulate(result, headers=["Mã thể loại", "Tên thể loại", "Số lượng sách"], tablefmt="github"))

