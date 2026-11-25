# Ask user for their name 
name = input("What is your name? ").strip().title()

# Remove whitespace from str
# name = name.strip()

# Remove whitespace from str and capitalize user's name
# name = name.strip().title()

# Capitalize user's name
# name = name.capitalize() 
# Explain by Vietnamese: Chuyển ký tự đầu tiên của chuỗi thành chữ hoa và các ký tự còn lại thành chữ thường
# name = name.title()
# Explain by Vietnamese: Chuyển ký tự đầu tiên của mỗi từ trong chuỗi thành chữ hoa và các ký tự còn lại thành chữ thường

#Split user's name into first and last name
first, last = name.split(" ")

# Say hello to user
print("Hello, " + first + "!")
print("Hello,", first + "!")
print(f"Hello, {first}!")
print("Hello, 'Friend'!")
print("Hello, \"Friend\"!")

"""
print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
Explain by Vietnamese:
- objects: các đối tượng cần in ra
- sep: chuỗi phân cách giữa các đối tượng (mặc định là khoảng trắng)
- end: chuỗi kết thúc sau khi in xong (mặc định là ký tự xuống dòng)
- file: tệp để in ra (mặc định là stdout)
- flush: có hay không flush buffer sau khi in (mặc định là False)
"""
# documentation: https://docs.python.org/3/library/functions.html
# documentation: https://docs.python.org/3/library/functions.html#print
# documentation: https://docs.python.org/3/library/stdtypes.html#string-methods

