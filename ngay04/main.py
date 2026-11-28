"""Ngày 4 – Bài 3 (15đ, cùng với tien_ich.py).

Import 3 hàm từ tien_ich.py và gọi thử cả ba.
Tự chạy thử: python main.py
"""

from tien_ich import xep_loai, la_nam_nhuan, dem_tu


def main():
    # xep_loai
    for diem in (9.5, 8, 7, 5, 3, 11):
        print(f"Điểm {diem}: {xep_loai(diem)}")

    # la_nam_nhuan
    for nam in (2024, 2023, 1900, 2000):
        print(f"Năm {nam} nhuận? {la_nam_nhuan(nam)}")

    # dem_tu
    van_ban = "Xin chào, xin chào bạn!"
    print(f"Đếm từ trong {van_ban!r}: {dem_tu(van_ban)}")


if __name__ == "__main__":
    main()