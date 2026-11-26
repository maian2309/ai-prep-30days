# print("Meow")
# print("Meow")
# print("Meow")

# i = 3
# while i!=0:
#     print("Meow")
#     i -= 1

# i = 1
# while i <= 3:
#     print("Meow")
#     i += 1

# for i in [0, 1, 2]:
#     print("Meow")

# for i in range(3):
#     print("Meow")

# print("Meow\n" * 3, end="")

# while True:
#     n = int(input("What's n? "))
#     if n > 0:
#         break

# for _ in range(n):
#     print("Meow")

def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            return n

def meow(n):
    for _ in range(n):
        print("Meow")

if __name__ == "__main__":
    main()