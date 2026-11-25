def main():
    tên = input("Tên của bạn là gì? ").strip().title()
    xin_chao(tên)

# Nhập rỗng → Xin chào, bạn! Viết code cho trường hợp người dùng không nhập gì cả
def xin_chao(ten):
    if ten == "":
        print("Xin chào, bạn!")
    else:
        print(f"Xin chào, {ten}!")

if __name__ == "__main__":
    main()