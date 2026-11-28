# Trả lời câu hỏi kiểm tra – Ngày 4

## Câu 1. Các khối `try / except / else / finally` chạy theo thứ tự nào? Khi nào cần `finally`?

Trả lời:

- `try` chạy trước.
- Nếu trong `try` có lỗi: phần còn lại của `try` bị bỏ qua, nhảy vào khối `except` khớp với loại lỗi.
- Nếu `try` không có lỗi: khối `else` chạy (bỏ qua `except`).
- `finally` **luôn chạy cuối cùng**, dù có lỗi hay không, dù lỗi có được bắt hay không, kể cả khi trong `try` có `return`.

Cần `finally` khi có việc **dọn dẹp bắt buộc phải làm**: đóng file, đóng kết nối mạng/cơ sở dữ liệu, giải phóng tài nguyên.

```python
f = open("data.txt")
try:
    noi_dung = f.read()
except OSError:
    print("Không đọc được file")
else:
    print("Đọc xong")
finally:
    f.close()   # luôn đóng file
```

## Câu 2. Vì sao không nên viết `except:` trống (không ghi loại lỗi)?

Trả lời:

`except:` trống bắt **mọi** lỗi, kể cả những lỗi không nên bắt:

- Lỗi do chính mình viết sai code (`NameError` khi gõ sai tên biến, `TypeError`...) bị giấu đi, chương trình chạy sai mà không biết vì sao, rất khó tìm lỗi.
- Bắt cả `KeyboardInterrupt` (Ctrl+C) và `SystemExit`, nên có khi không tắt được chương trình.

Nên ghi rõ loại lỗi mình dự đoán được, ví dụ `except ValueError:`, để lỗi bất ngờ vẫn hiện ra.

## Câu 3. venv giải quyết vấn đề gì? Không dùng thì chuyện gì có thể xảy ra khi bạn có 2 dự án?

Trả lời:

venv tạo một **môi trường Python riêng cho từng dự án**: thư viện cài vào `.venv` của dự án đó, không cài chung vào Python của cả máy.

Không dùng venv, hai dự án phải dùng chung một bộ thư viện. Ví dụ dự án A cần `requests==2.28`, dự án B cần `requests==2.34`: cài bản mới cho B thì A có thể bị hỏng. Ngoài ra cũng không biết rõ mỗi dự án thực sự cần những thư viện nào.

Dùng venv + `requirements.txt` thì mỗi dự án có đúng phiên bản nó cần, và người khác cài lại được y hệt bằng `pip install -r requirements.txt`.

## Câu 4. `if __name__ == "__main__":` dùng để làm gì? Điều gì xảy ra nếu bỏ nó đi trong `tien_ich.py`?

Trả lời:

- Khi chạy trực tiếp `python tien_ich.py`, biến `__name__` có giá trị `"__main__"`.
- Khi file khác `import tien_ich`, `__name__` có giá trị `"tien_ich"`.

Vì vậy code trong khối `if __name__ == "__main__":` **chỉ chạy khi chạy trực tiếp file**, không chạy khi bị import. Thường dùng để đặt code chạy thử.

Nếu bỏ đi và để code chạy thử ở ngoài, thì mỗi lần `main.py` import `tien_ich`, các lệnh chạy thử đó cũng chạy theo và in thêm kết quả không mong muốn. Như vậy là vi phạm yêu cầu "không được tự chạy gì khi bị import".

## Câu 5. `import math` và `from math import sqrt` khác nhau thế nào? Cách nào dễ trùng tên hơn?

Trả lời:

- `import math`: nạp cả module, khi dùng phải ghi tên module phía trước: `math.sqrt(9)`. Đọc vào là biết hàm lấy từ đâu.
- `from math import sqrt`: đưa thẳng tên `sqrt` vào file, gọi ngắn gọn `sqrt(9)`.

`from math import sqrt` **dễ trùng tên hơn**. Nếu trong file có hàm hoặc biến khác cũng tên `sqrt` (tự viết, hoặc import từ module khác), tên nào khai báo sau sẽ ghi đè tên trước. `from math import *` còn dễ trùng hơn nữa vì nhập hết mọi tên.
