def c_sang_f(c: float) -> float:
    return round(c * 9 / 5 + 32, 1)

def bmi(can_nang_kg: float, chieu_cao_m: float) -> float:
    return round(can_nang_kg / (chieu_cao_m ** 2), 1)

def main():
    print("Chuyển đổi nhiệt độ từ độ C sang độ F")
    c = float(input("Nhập nhiệt độ (°C): "))
    f = c_sang_f(c)
    print(f"{c}°C = {f}°F")
    print("Tính chỉ số BMI")
    can_nang = float(input("Nhập cân nặng (kg): "))
    chieu_cao = float(input("Nhập chiều cao (m): "))
    b = bmi(can_nang, chieu_cao)
    print(f"Chỉ số BMI của bạn là: {b}")

if __name__ == "__main__":
    main()