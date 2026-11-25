# Nhật ký Ngày 1

- Thời gian học thực tế: 2 giờ 15 phút
- 3 điều học được:
  1. **Xử lý chuỗi và in ra màn hình** (`hello.py`): dùng `input()` để nhận dữ liệu, nối các phương thức `.strip().title()` để bỏ khoảng trắng và viết hoa chữ cái đầu mỗi từ, dùng `.split(" ")` để tách họ và tên. Có 3 cách in lời chào: nối chuỗi bằng `+`, truyền nhiều đối số cho `print()` (tự thêm dấu cách nhờ `sep=' '`), và f-string `f"Hello, {first}!"` (gọn nhất). Muốn in dấu nháy kép bên trong chuỗi thì dùng `\"` hoặc bọc chuỗi bằng nháy đơn.
  2. **Làm việc với số** (`caculator.py`): `float()` chuyển chuỗi nhập vào thành số thực, `round(x / y, 2)` làm tròn đến 2 chữ số thập phân. Định dạng trong f-string: `f"{z:,}"` thêm dấu phẩy phân cách hàng nghìn, `f"{z:,.2f}"` vừa phân cách hàng nghìn vừa luôn hiện đúng 2 chữ số thập phân.
  3. **Tự viết hàm** (`hello_v2.py`, `caculator_v2.py`): dùng `def` để tạo hàm, đặt chương trình chính trong `main()` rồi gọi `main()` ở cuối file. Hàm có thể chỉ thực hiện hành động (`hello(name)` in ra màn hình) hoặc trả kết quả về bằng `return` (`square(n)` trả về `pow(n, 2)`). Nhờ đó code ngắn gọn, dễ đọc và tái sử dụng được.
- 1 điều còn chưa chắc:
  - `round()` đôi khi cho kết quả "lạ": `round(2.5)` ra `2` chứ không phải `3`, và `round(2.675, 2)` ra `2.67`. Cần tìm hiểu thêm về cách Python làm tròn (làm tròn về số chẵn) và lỗi biểu diễn số thực dấu phẩy động.
  - (Ghi chú thêm) `first, last = name.split(" ")` sẽ báo lỗi nếu người dùng chỉ nhập 1 từ hoặc nhập từ 3 từ trở lên — chưa biết cách xử lý trường hợp này.