"""Ngày 2 – Bài 5 (15đ): game đoán số.

- Máy chọn ngẫu nhiên một số từ 1 đến 100 (random.randint).
- Mỗi lượt: báo "Lớn hơn" hoặc "Nhỏ hơn".
- Tối đa 7 lượt; cuối game in số lần đã đoán (đoán trúng hay hết lượt đều in).
- Nhập chữ hoặc bỏ trống thì nhắc nhập lại, KHÔNG crash, KHÔNG tính lượt.

Tự chạy thử: python doan_so.py
"""


import random
def main():
    # Máy chọn ngẫu nhiên một số từ 1 đến 100
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 7

    while attempts < max_attempts:
        try:
            guess = int(input("Nhập số bạn đoán (1-100): "))
            attempts += 1

            if guess < secret_number:
                print("Lớn hơn!")
            elif guess > secret_number:
                print("Nhỏ hơn!")
            else:
                print(f"Chúc mừng! Bạn đã đoán đúng sau {attempts} lần.")
                return
        except ValueError:
            print("Vui lòng nhập một số hợp lệ.")

    print(f"Game over! Số cần đoán là {secret_number}. Bạn đã đoán {attempts} lần.")
    
if __name__ == "__main__":
    main()
