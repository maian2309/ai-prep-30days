"""Ngày 3 – List, dict, tuple, set. Bài 1, 2, 3, 5 (45 điểm).

Tự chạy thử: python cau_truc.py
"""


def dem_tu(van_ban: str) -> dict[str, int]:
    """Bài 1: đếm số lần xuất hiện của mỗi từ, không phân biệt hoa thường, bỏ dấu câu."""
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


def top_k(dem: dict[str, int], k: int) -> list[tuple[str, int]]:
    """Bài 2: k từ nhiều nhất, bằng số lần thì xếp theo chữ cái."""
    da_sap_xep = sorted(dem.items(), key=lambda x: (-x[1], x[0]))
    return da_sap_xep[:k]


def gop_khong_trung(a: list, b: list) -> list:
    """Bài 3: gộp a rồi b, bỏ trùng, giữ thứ tự xuất hiện đầu tiên."""
    ket_qua = []
    da_gap = set()
    for phan_tu in a + b:
        if phan_tu not in da_gap:
            da_gap.add(phan_tu)
            ket_qua.append(phan_tu)
    return ket_qua


def nhom_theo_chu_dau(ds: list[str]) -> dict[str, list[str]]:
    """Bài 5: nhóm theo chữ cái đầu (viết hoa), mỗi nhóm sắp xếp tăng dần."""
    ket_qua = {}
    for chuoi in ds:
        if chuoi:  # Bỏ qua chuỗi rỗng
            chu_dau = chuoi[0].upper()
            if chu_dau not in ket_qua:
                ket_qua[chu_dau] = []
            ket_qua[chu_dau].append(chuoi)
    # Sắp xếp từng nhóm tăng dần
    for chu_dau in ket_qua:
        ket_qua[chu_dau].sort()
    return ket_qua


def main():
    print(dem_tu("Học, học nữa, HỌC mãi!"))
    print(top_k({"b": 2, "a": 2, "c": 5}, 2))
    print(gop_khong_trung([3, 1, 3], [2, 1]))
    print(nhom_theo_chu_dau(["an", "Bình", "anh", ""]))


if __name__ == "__main__":
    main()