# def main():
#     print_colum(3)

# def print_colum(height):
#     # for _ in range(height):
#     #     print("#")
#     print("#\n" * height, end="")

# if __name__ == "__main__":  
#     main()

# def main():
#     print_row(4)

# def print_row(width):
#     print("?" * width) 

# if __name__ == "__main__":  
#     main()

def main():
    print_square(3)

def print_square(size):

    # # For each row in the square
    # for i in range(size):

    #     # For each column in the square
    #     for j in range(size):

    #         # Print brick
    #         print("#", end="")
    #     print()  # Move to the next line after printing a row
    for i in range(size):
        print("#" * size)  # Print a row of bricks

if __name__ == "__main__":
    main()