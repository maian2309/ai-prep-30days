def main():
    name = input("What is your name? ").strip().title()
    hello(name)

def hello(name):
    print(f"Hello, {name}!")

main()
