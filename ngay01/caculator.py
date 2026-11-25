x = float(input("What's x? "))
y = float(input("What's y? "))

z = round(x / y, 2)

print(f"{z:,}") # Định dạng số với dấu phẩy làm dấu phân cách hàng nghìn
# print(f"{z:,.2f}") # Định dạng số với dấu phẩy làm dấu phân cách hàng nghìn và 2 chữ số thập phân

# documentation: https://docs.python.org/3/library/functions.html#round

"""
round(number[, ndigits])
Explain by Vietnamese:
- number: số cần làm tròn
- ndigits: số chữ số thập phân cần làm tròn (mặc định là 0)
- Nếu ndigits > 0, làm tròn đến số chữ số thập phân đó
- Nếu ndigits = 0, làm tròn đến số nguyên gần nhất
- Nếu ndigits < 0, làm tròn đến bội số của 10^(-ndigits)
"""