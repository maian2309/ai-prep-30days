"""Ngày 2 – Điều kiện, vòng lặp. Bài 1–4 (45 điểm).

Tự chạy thử: python dieu_kien.py
Không dùng AI để viết code. Được hỏi AI giải thích khái niệm hoặc thông báo lỗi.
"""


def xep_loai(diem: float) -> str:
    """Bài 1 (15đ).

    >= 9   -> "Xuất sắc"
    >= 8   -> "Giỏi"
    >= 6.5 -> "Khá"
    >= 5   -> "Trung bình"
    < 5    -> "Yếu"
    Ngoài đoạn [0, 10] -> "Không hợp lệ"
    """
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
    """Bài 2 (10đ).

    Năm nhuận: chia hết cho 4 và không chia hết cho 100, hoặc chia hết cho 400.
    1900 -> False, 2000 -> True, 2024 -> True
    """
    if (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0):
        return True
    else:
        return False


def fizzbuzz(n: int) -> list[str]:
    """Bài 3 (10đ).

    Trả về list từ 1 đến n: bội của 3 là "Fizz", bội của 5 là "Buzz",
    bội của cả hai là "FizzBuzz", còn lại là số dạng chuỗi.
    fizzbuzz(5) == ["1", "2", "Fizz", "4", "Buzz"]
    """
    result = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    return result


def tam_giac(n: int) -> str:
    """Bài 4 (10đ).

    Tam giác căn phải cao n bằng ký tự "#", các dòng nối bằng "\\n",
    không có "\\n" ở cuối.
    tam_giac(3) == "  #\\n ##\\n###"
    """
    if n <= 0:
            return ""
    else:
        result = ""
        for i in range(1, n + 1):
            spaces = " " * (n - i)
            hashes = "#" * i
            result += spaces + hashes
            if i < n:
                result += "\n"
        return result


def main():
    # Tự gọi thử các hàm ở đây, ví dụ:
    print(xep_loai(8.5))
    print(la_nam_nhuan(2024))
    print(fizzbuzz(15))
    print(tam_giac(3))


if __name__ == "__main__":
    main()
