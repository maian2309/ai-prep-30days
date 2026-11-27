# Nhật ký Ngày 3

- Khởi động (5 câu Ngày 2, không nhìn bài): đúng 5/5 câu. Câu quên: không có
- Thời gian học thực tế: 2 giờ 15 phút
- 3 điều học được:
  1. Dùng dict để đếm số lần xuất hiện: nếu từ đã có trong dict thì cộng 1, chưa có thì gán bằng 1.
  2. `sorted(..., key=lambda x: (-x[1], x[0]))` cho phép sắp xếp theo nhiều tiêu chí: số lần giảm dần, bằng nhau thì theo chữ cái.
  3. Dùng set `da_gap` để kiểm tra phần tử đã gặp chưa, giúp loại trùng mà vẫn giữ thứ tự xuất hiện đầu tiên.
- 1 điều còn chưa chắc: khi nào một biến hay dữ liệu nhập vào có thể làm chương trình lỗi mà mình không để ý. Hôm nay mình gặp 3 lần:
  - `int(input())` ở menu danh bạ bị crash khi gõ chữ hoặc bỏ trống.
  - Đặt tên biến `dem_tu` trùng tên hàm: vẫn chạy nhưng dễ gây lỗi về sau.
  - VS Code tự thêm `from unittest import result` khi mình nhấn Enter chọn gợi ý.
  Cần tập thói quen thử dữ liệu xấu và đọc lại các dòng import trước khi commit.