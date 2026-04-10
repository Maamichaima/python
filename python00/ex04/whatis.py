import sys

def check_parity():
    if len(sys.argv) != 2:
        print("AssertionError: more than one argument is provided")
        exit()
    try:
        num = int(sys.argv[1])
    except ValueError:
        print("AssertionError: argument is not an integer")
        exit()

    num = int(sys.argv[1])

    if num % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")

if __name__ == "__main__":
    check_parity()

