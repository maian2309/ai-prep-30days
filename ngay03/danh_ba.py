"""Ngày 3 – Bài 4 (15đ): danh bạ dòng lệnh.

- Lưu trong một dict: tên -> số điện thoại.
- Menu: 1. Thêm  2. Sửa  3. Xóa  4. Tìm  5. Liệt kê  0. Thoát
- Tìm theo MỘT PHẦN tên, không phân biệt hoa thường
  (gõ "an" tìm ra cả "Nguyễn An" và "Lan").
- Sửa/xóa tên không có trong danh bạ thì báo, KHÔNG crash.
- Chọn sai số menu thì báo và hiện lại menu.

Tự chạy thử: python danh_ba.py
"""


def main():
    """Chương trình chính, chạy menu cho đến khi chọn 0."""
    danh_ba = {}
    while True:
        print("\nMenu:")
        print("1. Thêm")
        print("2. Sửa")
        print("3. Xóa")
        print("4. Tìm")
        print("5. Liệt kê")
        print("0. Thoát")
        lua_chon = input("Chọn số: ").strip()
        if lua_chon == "1":
            them(danh_ba)
        elif lua_chon == "2":
            sua(danh_ba)
        elif lua_chon == "3":
            xoa(danh_ba)
        elif lua_chon == "4":
            tim(danh_ba)
        elif lua_chon == "5":
            liet_ke(danh_ba)
        elif lua_chon == "0":
            print("Thoát chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng thử lại.")

def them(danh_ba: dict):
    """Thêm một tên và số điện thoại vào danh bạ."""
    ten = input("Nhập tên: ")
    so_dien_thoai = input("Nhập số điện thoại: ")
    danh_ba[ten] = so_dien_thoai
    print(f"Đã thêm {ten}: {so_dien_thoai}")

def sua(danh_ba: dict):
    """Sửa số điện thoại của một tên trong danh bạ."""
    ten = input("Nhập tên cần sửa: ")
    if ten in danh_ba:
        so_dien_thoai_moi = input("Nhập số điện thoại mới: ")
        danh_ba[ten] = so_dien_thoai_moi
        print(f"Đã sửa {ten}: {so_dien_thoai_moi}")
    else:
        print(f"{ten} không có trong danh bạ.")

def xoa(danh_ba: dict):
    """Xóa một tên khỏi danh bạ."""
    ten = input("Nhập tên cần xóa: ")
    if ten in danh_ba:
        del danh_ba[ten]
        print(f"Đã xóa {ten} khỏi danh bạ.")
    else:
        print(f"{ten} không có trong danh bạ.")

def tim(danh_ba: dict):
    """Tìm kiếm tên trong danh bạ."""
    tu_khoa = input("Nhập tên cần tìm: ")
    tim_thay = []
    for ten, so in danh_ba.items():
        if tu_khoa.lower() in ten.lower():
            tim_thay.append((ten, so))
    if tim_thay:
        for ten, so in tim_thay:
            print(f"{ten}: {so}")
    else:
        print(f"Không tìm thấy tên chứa '{tu_khoa}'.")


def liet_ke(danh_ba: dict):
    """Liệt kê tất cả các mục trong danh bạ."""
    if danh_ba:
        for ten, so in danh_ba.items():
            print(f"{ten}: {so}")
    else:
        print("Danh bạ trống.")

if __name__ == "__main__":
    main()
