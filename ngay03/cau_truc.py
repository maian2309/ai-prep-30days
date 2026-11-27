"""Ngày 3 – List, dict, tuple, set. Bài 1, 2, 3, 5 (45 điểm).

Tự chạy thử: python cau_truc.py
Không dùng AI để viết code. Được hỏi AI giải thích khái niệm hoặc thông báo lỗi.
"""


def dem_tu(van_ban: str) -> dict[str, int]:
    """Bài 1 (15đ).

    Đếm số lần xuất hiện của mỗi từ.
    - Không phân biệt hoa thường.
    - Bỏ các dấu câu . , ! ? ; :
    - Tách theo khoảng trắng.
    dem_tu("Học, học nữa, HỌC mãi!") == {"học": 3, "nữa": 1, "mãi": 1}
    dem_tu("") == {}
    """
    if not van_ban:
        return {}
    else:
        # Xóa các dấu câu
        for char in ".,!?;:":
            van_ban = van_ban.replace(char, "")
        # Chuyển về chữ thường và tách từ
        danh_sach_tu = van_ban.lower().split()
        # Đếm số lần xuất hiện của mỗi từ
        dem = {}
        for tu in danh_sach_tu:
            if tu in dem:
                dem[tu] += 1
            else:
                dem[tu] = 1
        return dem
    


def top_k(dem: dict[str, int], k: int) -> list[tuple[str, int]]:
    """Bài 2 (10đ).

    Trả về k cặp (từ, số lần) xuất hiện nhiều nhất, xếp giảm dần theo số lần.
    Bằng số lần thì xếp theo thứ tự chữ cái của từ.
    k lớn hơn số từ thì trả về hết.
    top_k({"b": 2, "a": 2, "c": 5}, 2) == [("c", 5), ("a", 2)]
    """
    if not dem:
        return []
    else:
        # Sắp xếp theo số lần giảm dần, nếu bằng nhau thì theo thứ tự chữ cái
        sorted_items = sorted(dem.items(), key=lambda x: (-x[1], x[0]))
        return sorted_items[:k]


def gop_khong_trung(a: list, b: list) -> list:
    """Bài 3 (10đ).

    Gộp a rồi đến b, bỏ phần tử trùng, giữ thứ tự xuất hiện đầu tiên.
    gop_khong_trung([3, 1, 3], [2, 1]) == [3, 1, 2]
    """
    if not a and not b:
        return []
    else:
        # Gộp hai danh sách và loại bỏ phần tử trùng, giữ thứ tự xuất hiện đầu tiên
        result = []
        seen = set()
        for item in a + b:
            if item not in seen:
                seen.add(item)
                result.append(item)
        return result



def nhom_theo_chu_dau(ds: list[str]) -> dict[str, list[str]]:
    """Bài 5 (10đ).

    Nhóm các chuỗi theo chữ cái đầu (key viết hoa), mỗi nhóm sắp xếp tăng dần.
    Bỏ qua chuỗi rỗng.
    nhom_theo_chu_dau(["an", "Bình", "anh", ""]) == {"A": ["an", "anh"], "B": ["Bình"]}
    """
    if not ds:
        return {}
    else:
        result = {}
        for chuoi in ds:
            if chuoi:  # Bỏ qua chuỗi rỗng
                key = chuoi[0].upper()  # Lấy chữ cái đầu và viết hoa
                if key not in result:
                    result[key] = []
                result[key].append(chuoi)
        # Sắp xếp từng nhóm tăng dần
        for key in result:
            result[key].sort()
        return result

def main():
    print(dem_tu("Học, học nữa, HỌC mãi!"))
    print(top_k({"b": 2, "a": 2, "c": 5}, 2))
    print(gop_khong_trung([3, 1, 3], [2, 1]))
    print(nhom_theo_chu_dau(["an", "Bình", "anh", ""]))


if __name__ == "__main__":
    main()
