"""Ngày 4 – Bài 4 (15đ): thư viện requests + venv.

Chuẩn bị (chạy trong Git Bash, đứng ở thư mục ngay04):
    python -m venv .venv
    source .venv/Scripts/activate
    pip install requests
    pip freeze > requirements.txt

Cách chạy:  python github_info.py maian2309

Yêu cầu:
- Lấy username từ sys.argv.
- Gọi https://api.github.com/users/<username>
- In: tên (name), số repo public (public_repos), ngày tạo tài khoản (created_at).
- Xử lý 3 lỗi, mỗi lỗi in thông báo rõ ràng, KHÔNG hiện traceback:
    1. Thiếu tham số (chạy: python github_info.py)
    2. User không tồn tại (mã 404)
    3. Mất mạng hoặc quá thời gian chờ (dùng timeout=10)
"""

import sys

try:
    import requests
except ImportError:
    print("Lỗi: chưa cài thư viện requests.")
    print("Hãy kích hoạt venv (source .venv/Scripts/activate) rồi chạy: pip install requests")
    sys.exit(1)


def main():
    # Lỗi 1: thiếu tham số
    if len(sys.argv) < 2:
        print("Lỗi: thiếu username.")
        print("Cách dùng: python github_info.py <username>")
        sys.exit(1)

    username = sys.argv[1].strip()
    url = f"https://api.github.com/users/{username}"

    # Lỗi 3: mất mạng hoặc quá thời gian chờ
    try:
        phan_hoi = requests.get(url, timeout=10)
    except requests.exceptions.Timeout:
        print("Lỗi: quá thời gian chờ (10 giây). Hãy thử lại sau.")
        sys.exit(1)
    except requests.exceptions.ConnectionError:
        print("Lỗi: không kết nối được tới GitHub. Hãy kiểm tra mạng.")
        sys.exit(1)
    except requests.exceptions.RequestException as loi:
        print(f"Lỗi khi gọi API: {loi}")
        sys.exit(1)

    # Lỗi 2: user không tồn tại
    if phan_hoi.status_code == 404:
        print(f"Lỗi: không tìm thấy user '{username}' trên GitHub.")
        sys.exit(1)

    # Các lỗi HTTP khác (ví dụ 403 do gọi API quá nhiều lần)
    if phan_hoi.status_code != 200:
        print(f"Lỗi: GitHub trả về mã {phan_hoi.status_code}.")
        sys.exit(1)

    du_lieu = phan_hoi.json()
    ten = du_lieu.get("name") or "(chưa đặt tên)"
    so_repo = du_lieu.get("public_repos", 0)
    ngay_tao = (du_lieu.get("created_at") or "")[:10]  # "2023-01-15T08:00:00Z" -> "2023-01-15"

    print(f"Username     : {username}")
    print(f"Tên          : {ten}")
    print(f"Repo public  : {so_repo}")
    print(f"Ngày tạo     : {ngay_tao}")


if __name__ == "__main__":
    main()