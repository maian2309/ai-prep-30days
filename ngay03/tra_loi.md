# Trả lời câu hỏi kiểm tra – Ngày 3

## Câu 1. List và tuple khác nhau ở điểm nào quan trọng nhất? Khi nào nên dùng tuple?

Trả lời:
Điểm khác quan trọng nhất là list có thể thay đổi (mutable): thêm, xóa, sửa phần tử sau khi tạo. Tuple không thể thay đổi (immutable): tạo xong thì giữ nguyên.

Nên dùng tuple khi dữ liệu là một bộ giá trị cố định, không cần sửa, ví dụ tọa độ `(x, y)`, cặp `(từ, số lần)`, hoặc khi cần dùng làm key của dict / phần tử của set. Tuple cũng giúp người đọc code hiểu là dữ liệu này không bị thay đổi.


## Câu 2. Sau `a = [1, 2]; b = a; b.append(3)` thì `a` là gì? Làm sao để `b` là bản sao độc lập?

Trả lời:
`a` là `[1, 2, 3]`. Phép gán `b = a` không tạo list mới mà chỉ cho `b` trỏ cùng một đối tượng list với `a`, nên sửa qua `b` thì `a` cũng thay đổi.

Để `b` là bản sao độc lập: `b = a.copy()`, hoặc `b = a[:]`, hoặc `b = list(a)`. Nếu list chứa list lồng bên trong thì dùng `copy.deepcopy(a)` để sao chép cả các phần tử bên trong.


## Câu 3. Vì sao list không làm key của dict được, còn tuple thì được?

Trả lời:
Key của dict phải hashable, tức là có giá trị băm (hash) không đổi trong suốt vòng đời. Dict dùng hash để tìm key nhanh. List có thể thay đổi nội dung nên hash sẽ đổi theo, làm dict không tìm lại được key; vì vậy Python không cho list làm key (báo `TypeError: unhashable type: 'list'`).

Tuple không thể thay đổi nên có hash ổn định, do đó làm key được. Lưu ý: tuple chỉ hashable khi mọi phần tử bên trong cũng hashable (ví dụ `(1, [2])` thì không).


## Câu 4. Kiểm tra `x in ...` trên list 1 triệu phần tử và trên set 1 triệu phần tử khác nhau thế nào về tốc độ? Vì sao?

Trả lời:
Với set, `x in` nhanh hơn rất nhiều. Với list, Python phải duyệt lần lượt từng phần tử cho đến khi gặp `x` hoặc hết list, nên độ phức tạp là O(n), trường hợp xấu nhất phải so sánh khoảng 1 triệu lần.

Set được cài đặt bằng bảng băm (hash table): Python tính hash của `x`, nhảy thẳng đến vị trí tương ứng để kiểm tra, nên trung bình chỉ O(1), gần như không phụ thuộc số phần tử. Vì vậy khi cần kiểm tra tồn tại nhiều lần, nên chuyển dữ liệu sang set.


## Câu 5. Viết list comprehension tạo bình phương các số chẵn từ 0 đến 20, rồi giải thích từng phần của câu lệnh.

Trả lời:

```python
[x ** 2 for x in range(0, 21) if x % 2 == 0]
```

Kết quả: `[0, 4, 16, 36, 64, 100, 144, 196, 256, 324, 400]`

Giải thích từng phần:
- `range(0, 21)`: sinh các số nguyên từ 0 đến 20 (21 không được tính).
- `for x in range(0, 21)`: lần lượt gán từng số đó cho biến `x`.
- `if x % 2 == 0`: điều kiện lọc, chỉ giữ lại những `x` chia hết cho 2 (số chẵn).
- `x ** 2`: biểu thức tính cho mỗi `x` được giữ lại, ở đây là bình phương của `x`; giá trị này là phần tử được đưa vào list kết quả.
- Cặp ngoặc `[...]`: gom tất cả kết quả thành một list mới.
