# Nhật ký Ngày 4

- Khởi động (5 câu Ngày 3, không nhìn bài): đúng 5/5 câu. Câu quên:
- Thời gian học thực tế: khoảng 3 giờ 15 phút
- 3 điều học được:
  1. Dùng `try / except` để bắt đúng loại lỗi (`ValueError`, `TypeError`), kết hợp vòng lặp `while True` để hỏi lại người dùng cho tới khi nhập đúng; chủ động `raise` lỗi khi tham số không hợp lệ.
  2. Tách code thành module: đặt hàm vào `tien_ich.py`, dùng `from tien_ich import ...` trong `main.py`, và dùng `if __name__ == "__main__":` để file không tự chạy khi bị import.
  3. Tạo môi trường ảo bằng `venv`, cài thư viện `requests`, lưu phiên bản vào `requirements.txt`; gọi API GitHub với `timeout=10`, đọc `sys.argv`, kiểm tra `status_code` và xử lý lỗi mạng mà không hiện traceback.
- 1 điều còn chưa chắc: Vì sao `bool` lại là lớp con của `int` (nên `isinstance(True, int)` ra `True`), và khi nào nên bắt lỗi ngay trong hàm, khi nào nên `raise` để nơi gọi hàm tự xử lý.

## Bài 5: giải thích .gitignore (10đ)

File `.gitignore` ở thư mục gốc repo đã có sẵn 3 dòng dưới đây. Giải thích vì sao từng dòng phải có:

- `.venv/`: Thư mục môi trường ảo rất nặng (hàng nghìn file thư viện), và chứa đường dẫn riêng của máy mình nên máy khác dùng không được. Không cần đưa lên git: người khác chỉ cần `requirements.txt` để tự tạo lại bằng `python -m venv .venv` rồi `pip install -r requirements.txt`.
- `__pycache__/`: Chứa các file `.pyc` do Python tự sinh ra khi import module, để lần sau chạy nhanh hơn. Các file này tạo lại được bất cứ lúc nào và khác nhau theo phiên bản Python, nên đưa lên git chỉ làm repo thêm rác và thay đổi lặt vặt.
- `.env`: Chứa thông tin bí mật như API key, mật khẩu, token. Nếu đẩy lên GitHub thì ai cũng xem được và có thể lấy dùng, gây lộ tài khoản hoặc mất tiền.

Kiểm tra: sau khi tạo `.venv` ở bài 4, chạy `git status`. Thư mục `.venv` KHÔNG được hiện ra. Ghi kết quả bạn thấy:

```
$ git status
On branch main
Your branch is up to date with 'origin/main'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   ../ngay01/hoa_don.py
        modified:   ../ngay03/cau_truc.py

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        ./

no changes added to commit (use "git add" and/or "git commit -a")
```

Nhận xét: `.venv/` không hiện ra trong kết quả. Thư mục `ngay04` chưa được add lần nào nên git chỉ hiện gọn là `./`; `.venv/` và `__pycache__/` đã bị `.gitignore` bỏ qua nên sẽ không bị add khi chạy `git add .`.
