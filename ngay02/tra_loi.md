# Trả lời câu hỏi kiểm tra – Ngày 2

## Câu 1. `for` và `while`: khi nào dùng cái nào? Mỗi loại một ví dụ.

Trả lời:

- **`for`**: dùng khi **biết trước** số lần lặp, hoặc cần duyệt qua từng phần tử của một dãy (list, chuỗi, `range`, ...).
- **`while`**: dùng khi **không biết trước** số lần lặp, chỉ biết **điều kiện** để tiếp tục (lặp cho đến khi điều kiện sai).

Ví dụ `for` – in bảng cửu chương 5:

```python
for i in range(1, 11):
    print(f"5 x {i} = {5 * i}")
```

Ví dụ `while` – bắt người dùng nhập đến khi đúng mật khẩu:

```python
mat_khau = ""
while mat_khau != "python123":
    mat_khau = input("Nhập mật khẩu: ")
print("Đăng nhập thành công!")
```

Lưu ý: với `while` phải chắc chắn điều kiện sẽ có lúc sai, nếu không sẽ bị **vòng lặp vô hạn**.

## Câu 2. `break` và `continue` khác nhau thế nào?

Trả lời:

| Lệnh | Tác dụng |
|---|---|
| `break` | **Thoát hẳn** khỏi vòng lặp, không chạy các lần lặp còn lại. |
| `continue` | **Bỏ qua phần còn lại của lần lặp hiện tại**, nhảy sang lần lặp kế tiếp. |

Ví dụ:

```python
for i in range(1, 6):
    if i == 3:
        break
    print(i)
# Kết quả: 1 2  (gặp 3 thì dừng hẳn)

for i in range(1, 6):
    if i == 3:
        continue
    print(i)
# Kết quả: 1 2 4 5  (chỉ bỏ qua số 3)
```

## Câu 3. `range(1, 10, 3)` sinh ra những số nào? `range(10, 0, -2)` thì sao?

Trả lời:

`range(start, stop, step)` bắt đầu từ `start`, cộng thêm `step` mỗi lần, và **không bao gồm** `stop`.

- `range(1, 10, 3)` → **1, 4, 7** (số tiếp theo là 10 = `stop` nên dừng).
- `range(10, 0, -2)` → **10, 8, 6, 4, 2** (bước âm nên đếm lùi; số tiếp theo là 0 = `stop` nên dừng).

Kiểm tra:

```python
print(list(range(1, 10, 3)))    # [1, 4, 7]
print(list(range(10, 0, -2)))   # [10, 8, 6, 4, 2]
```

## Câu 4. Kể ít nhất 4 giá trị được coi là False trong `if`.

Trả lời:

Các giá trị "falsy" (bị coi là `False`):

1. `False`
2. `None`
3. Số 0: `0`, `0.0`
4. Chuỗi rỗng: `""`
5. List rỗng: `[]`
6. Tuple rỗng: `()`
7. Dict rỗng: `{}`
8. Set rỗng: `set()`

Ví dụ:

```python
ten = ""
if not ten:
    print("Bạn chưa nhập tên!")   # chạy vì "" được coi là False
```

Mọi giá trị khác (số khác 0, chuỗi có ký tự, list có phần tử, ...) đều được coi là `True`. Chú ý: chuỗi `"0"` hay `"False"` vẫn là **True** vì không rỗng.

## Câu 5. Vì sao thứ tự các `elif` trong `xep_loai` quan trọng? Đảo thứ tự thì sai ở đâu?

Trả lời:

Python kiểm tra các điều kiện `if` / `elif` **từ trên xuống dưới** và **chỉ chạy nhánh đầu tiên đúng**, các nhánh sau bị bỏ qua. Vì các điều kiện kiểu `diem >= ...` **lồng nhau** (điểm ≥ 8 thì chắc chắn cũng ≥ 6.5, ≥ 5), nên phải xét từ ngưỡng **cao xuống thấp**.

Thứ tự đúng:

```python
def xep_loai(diem):
    if diem >= 8:
        return "Giỏi"
    elif diem >= 6.5:
        return "Khá"
    elif diem >= 5:
        return "Trung bình"
    else:
        return "Yếu"

print(xep_loai(9))   # Giỏi ✅
```

Nếu đảo thứ tự (thấp lên cao):

```python
def xep_loai_sai(diem):
    if diem >= 5:
        return "Trung bình"
    elif diem >= 6.5:
        return "Khá"
    elif diem >= 8:
        return "Giỏi"
    else:
        return "Yếu"

print(xep_loai_sai(9))   # Trung bình ❌
```

**Sai ở đâu:** điểm 9 thỏa ngay điều kiện đầu tiên `diem >= 5` nên trả về "Trung bình" và dừng luôn. Các nhánh "Khá", "Giỏi" **không bao giờ được chạy tới** với bất kỳ điểm nào ≥ 5 — chúng trở thành code "chết".

(Cách khác để thứ tự không còn quan trọng là viết điều kiện theo khoảng, ví dụ `6.5 <= diem < 8`, nhưng cách xét từ cao xuống thấp gọn hơn.)
