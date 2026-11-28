"""Ngày 4 – Bài 3 (15đ, cùng với main.py): module tiện ích.

Chép 3 hàm bạn đã viết vào đây:
  - xep_loai   (Ngày 2, dieu_kien.py)
  - la_nam_nhuan (Ngày 2, dieu_kien.py)
  - dem_tu     (Ngày 3, cau_truc.py)
File này KHÔNG được tự chạy gì khi bị import.
"""

def xep_loai(diem: float) -> str:
    if diem < 0 or diem > 10:
        return "Không hợp lệ"
    elif diem >= 9:
        return "Xuất sắc"
    elif diem >= 8:
        return "Giỏi"
    elif diem >= 6.5:
        return "Khá"
    elif diem >= 5:
        return "Trung bình"
    else:
        return "Yếu"

def la_nam_nhuan(nam: int) -> bool:
    return (nam % 4 == 0 and nam % 100 != 0) or nam % 400 == 0

def dem_tu(van_ban: str) -> dict[str, int]:
    # Xóa các dấu câu
    for ky_tu in ".,!?;:":
        van_ban = van_ban.replace(ky_tu, "")
    # Đếm số lần xuất hiện của mỗi từ
    dem = {}
    for tu in van_ban.lower().split():
        if tu in dem:
            dem[tu] += 1
        else:
            dem[tu] = 1
    return dem

if __name__ == "__main__":
    # Chỉ chạy khi gõ: python tien_ich.py (tự thử nhanh 3 hàm ở đây)
    pass
