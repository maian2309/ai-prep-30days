""" chia_hoa_don(tong: int, so_nguoi: int, tip_phan_tram:
float) -> int . Cộng tip, chia đều, làm tròn lên bội số 1.000đ.
chia_hoa_don(1_000_000, 3, 10) == 367000 , chia_hoa_don(500_000, 4, 0) ==
125000 . Gợi ý: math.ceil .
"""
import math

def chia_hoa_don(tong: int, so_nguoi: int, tip_phan_tram: float) -> int:
    total_with_tip = tong + (tong * tip_phan_tram / 100)
    amount_per_person = total_with_tip / so_nguoi
    return math.ceil(amount_per_person / 1000) * 1000

def main():
    tong = int(input("Nhập tổng hóa đơn (VNĐ): "))
    so_nguoi = int(input("Nhập số người: "))
    tip_phan_tram = float(input("Nhập phần trăm tip (%): "))
    tien_moi_nguoi = chia_hoa_don(tong, so_nguoi, tip_phan_tram)
    print(f"Mỗi người cần trả: {tien_moi_nguoi:,} VNĐ")
    

if __name__ == "__main__":
    main()