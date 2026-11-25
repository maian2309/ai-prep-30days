import math

def chia_hoa_don(tong: int, so_nguoi: int, tip_phan_tram: float) -> int:
    tong_co_tip = tong + tong * tip_phan_tram / 100
    moi_nguoi = tong_co_tip / so_nguoi
    return math.ceil(moi_nguoi / 1000) * 1000

def main():
    tong = int(input("Nhập tổng hóa đơn (VNĐ): "))
    so_nguoi = int(input("Nhập số người: "))
    tip_phan_tram = float(input("Nhập phần trăm tip (%): "))
    print(f"Mỗi người cần trả: {chia_hoa_don(tong, so_nguoi, tip_phan_tram):,} VNĐ")

if __name__ == "__main__":
    main()