"""Ngày 4 – Xử lý lỗi. Bài 1 và Bài 2 (20 điểm).

Tự chạy thử: python an_toan.py
Không dùng AI để viết code. Được hỏi AI giải thích khái niệm hoặc thông báo lỗi.
"""


def nhap_so_nguyen(loi_nhac: str, nho_nhat: int, lon_nhat: int) -> int:
    """Bài 1 (10đ).

    Hỏi bằng input(loi_nhac) cho tới khi người dùng nhập một số nguyên
    trong đoạn [nho_nhat, lon_nhat], rồi trả về số đó (kiểu int).
    Mỗi lần nhập sai thì in LÝ DO cụ thể, ví dụ:
    - "abc"  -> "Phải nhập số nguyên."
    - "150"  -> "Phải nằm trong khoảng 1–100."
    """
    if nho_nhat > lon_nhat:
        raise ValueError("nho_nhat không được lớn hơn lon_nhat")

    while True:
        chuoi = input(loi_nhac).strip()

        try:
            so = int(chuoi)
        except ValueError:
            print("Phải nhập số nguyên.")
            continue

        if not (nho_nhat <= so <= lon_nhat):
            print(f"Phải nằm trong khoảng {nho_nhat}–{lon_nhat}.")
            continue

        return so


def chia_an_toan(a, b) -> float:
    """Bài 2 (10đ).

    Trả về a / b.
    - b == 0 -> raise ValueError("Không thể chia cho 0")
    - a hoặc b không phải số (int/float) -> raise TypeError
    chia_an_toan(7, 2) == 3.5
    """
    for ten, gia_tri in (("a", a), ("b", b)):
        # bool là lớp con của int trong Python, nên loại riêng ra
        if isinstance(gia_tri, bool) or not isinstance(gia_tri, (int, float)):
            raise TypeError(
                f"{ten} phải là số (int hoặc float), "
                f"nhận được {type(gia_tri).__name__}"
            )

    if b == 0:
        raise ValueError("Không thể chia cho 0")

    return a / b


def main():
    # Bài 1
    tuoi = nhap_so_nguyen("Nhập tuổi (1-120): ", 1, 120)
    print("Tuổi của bạn:", tuoi)

    # Bài 2: trường hợp đúng
    print("7 / 2 =", chia_an_toan(7, 2))

    # Bài 2: các trường hợp lỗi
    for a, b in [(7, 0), ("7", 2), (7, None)]:
        try:
            chia_an_toan(a, b)
        except (ValueError, TypeError) as loi:
            print(f"chia_an_toan({a!r}, {b!r}) -> {type(loi).__name__}: {loi}")


if __name__ == "__main__":
    main()
