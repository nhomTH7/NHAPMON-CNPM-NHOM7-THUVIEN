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
    print("\n📌 Báo cáo sách hỏng/mất:")
    print(tabulate(result, headers=["Mã sách", "Tên sách", "Hỏng", "Mất"], tablefmt="github"))
    