# Trả lời câu hỏi kiểm tra – Ngày 1

## Câu 1. `print()` và `return` khác nhau thế nào? Cho ví dụ một hàm in ra màn hình nhưng trả về `None`.

Trả lời:

- `print()` chỉ **hiển thị** giá trị lên màn hình cho người xem. Chương trình không lấy lại được giá trị đó để dùng tiếp.
- `return` **trả giá trị về** cho nơi gọi hàm. Giá trị này có thể gán vào biến, tính toán tiếp hoặc truyền vào hàm khác. Khi gặp `return`, hàm kết thúc ngay.
- Hàm không có `return` (hoặc chỉ có `return` trống) sẽ tự động trả về `None`.

Ví dụ:

```python
def chao(ten):
    print("Xin chào", ten)   # chỉ in ra, không return

ket_qua = chao("An")         # màn hình hiện: Xin chào An
print(ket_qua)               # None
```

So sánh với hàm có `return`:

```python
def cong(a, b):
    return a + b

x = cong(2, 3)   # không in gì
print(x * 10)    # 50, vì dùng được giá trị trả về
```


## Câu 2. Vì sao `"5" + "5"` ra `"55"` còn `5 + 5` ra `10`? `input()` luôn trả về kiểu gì?

Trả lời:

Toán tử `+` làm việc khác nhau tùy theo kiểu dữ liệu:

- Với **chuỗi** (`str`), `+` là **nối chuỗi**, nên `"5" + "5"` → `"55"`.
- Với **số** (`int`, `float`), `+` là **phép cộng**, nên `5 + 5` → `10`.

`input()` **luôn trả về kiểu `str`**, kể cả khi người dùng gõ vào một con số. Muốn tính toán thì phải ép kiểu:

```python
a = input("Nhập số: ")       # gõ 5 → a = "5" (str)
print(a + a)                 # "55"

b = int(input("Nhập số: "))  # gõ 5 → b = 5 (int)
print(b + b)                 # 10
```


## Câu 3. Sau `a = 3; b = a; a = 4` thì `b` bằng bao nhiêu? Giải thích bằng khái niệm "biến là tên gắn với object".

Trả lời:

`b` bằng **3**.

Trong Python, biến không phải "chiếc hộp chứa giá trị" mà là **cái tên (nhãn) gắn vào một object** trong bộ nhớ:

1. `a = 3`: tạo object `3` và gắn tên `a` vào nó.
2. `b = a`: gắn thêm tên `b` vào **cùng object** mà `a` đang trỏ tới, tức object `3`.
3. `a = 4`: tạo object `4` rồi **chuyển nhãn `a`** sang object mới. Lệnh này không làm thay đổi object `3`.

Nhãn `b` vẫn gắn với object `3`, nên `b == 3`. Phép gán chỉ di chuyển tên, không sửa object cũ (hơn nữa số nguyên là kiểu bất biến, không sửa được).

```
Sau bước 2:   a ──┐
                  ├──► 3
              b ──┘

Sau bước 3:   a ─────► 4
              b ─────► 3
```


## Câu 4. Tham số (parameter) và đối số (argument) khác nhau thế nào?

Trả lời:

- **Tham số (parameter)** là tên biến được khai báo trong **định nghĩa hàm**, giống như "chỗ trống" chờ nhận giá trị.
- **Đối số (argument)** là giá trị cụ thể được truyền vào **khi gọi hàm**.

```python
def binh_phuong(x):    # x là tham số
    return x * x

binh_phuong(7)         # 7 là đối số
```

Khi gọi hàm, đối số được gán cho tham số tương ứng.


## Câu 5. Ba lệnh `git add`, `git commit`, `git push`, mỗi lệnh làm gì?

Trả lời:

| Lệnh | Tác dụng |
|---|---|
| `git add <file>` | Đưa thay đổi của file vào **vùng chuẩn bị (staging area)**, tức là chọn những thay đổi sẽ được lưu ở lần commit tới. `git add .` chọn tất cả thay đổi. |
| `git commit -m "lời nhắn"` | **Lưu một "ảnh chụp" (snapshot)** các thay đổi đã `add` vào lịch sử của repo **trên máy mình (local)**, kèm lời nhắn mô tả. |
| `git push` | **Đẩy các commit** từ repo local lên **repo từ xa (remote)**, ví dụ GitHub, để người khác thấy và để có bản sao lưu. |

Quy trình thường dùng:

```bash
git add bai_tap.py
git commit -m "Hoàn thành bài tập ngày 1"
git push
```

Tóm lại: **add** = chọn thay đổi → **commit** = lưu vào lịch sử trên máy → **push** = gửi lên server.
