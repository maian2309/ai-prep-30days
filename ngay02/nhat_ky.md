# Nhật ký Ngày 2

- Khởi động (5 câu Ngày 1, không nhìn bài): đúng 5/5 câu. Câu quên: ___
- Thời gian học thực tế: khoảng 2 giờ
- Đã làm:
  - Bài theo bài giảng: `compare.py`, `grade.py`, `parity.py`, `house.py`, `cat.py`, `mario.py`, `hogwarts.py`
  - Bài tập: `dieu_kien.py` (bài 1–4: `xep_loai`, `la_nam_nhuan`, `fizzbuzz`, `tam_giac`), `doan_so.py` (bài 5: game đoán số)
  - Trả lời 5 câu hỏi kiểm tra: `tra_loi.md`
- 3 điều học được:
  1. `if` / `elif` / `else` chạy nhánh **đầu tiên** đúng, nên thứ tự điều kiện quan trọng (xét ngưỡng từ cao xuống thấp như trong `xep_loai`). Có thể dùng `match ... case` thay cho chuỗi `elif` so sánh bằng (`house.py`).
  2. `for` dùng khi biết trước số lần lặp hoặc duyệt một dãy (`range`, list, dict); `while` dùng khi chỉ biết điều kiện dừng. Mẫu `while True` + `break`/`return` dùng để bắt nhập lại đến khi hợp lệ (`cat.py`).
  3. Dùng `try` / `except ValueError` để chương trình không bị crash khi người dùng nhập chữ thay vì số (`doan_so.py`). Tách code thành các hàm nhỏ và đặt `main()` trong `if __name__ == "__main__":`.
- 1 điều còn chưa chắc: khi nào nên dùng list, dict, hay list chứa dict (`hogwarts.py`), và cách duyệt từng loại cho gọn.

## Ghi chú cần sửa
- `doan_so.py`: khi hết lượt mới in số cần đoán, **chưa in số lần đã đoán** như đề yêu cầu. Số ngoài khoảng 1–100 vẫn bị tính một lượt.
- `dieu_kien.py`: vòng `while True` trong `xep_loai` không cần thiết (hàm đã `return` ngay). Các dòng `pass` sau `return` có thể xoá.
