from ft_filter import ft_filter
import sys


def main():
    # print(len(sys.argv))
    if len(sys.argv) != 3:
        print("AssertionError: the arguments are bad")
        exit()
    if type(sys.argv[1]) != str or not sys.argv[2].isdigit():
        print("AssertionError: the arguments are bad")
        exit()
    argv = sys.argv[1]
    words = argv.split(" ")
    n = int(sys.argv[2])
    filtered_gen = ft_filter(lambda word: len(word) >= n, words)

    result = [word for word in filtered_gen]
    print(f"result: {list(result)}")
    # print(n)

if __name__ == "__main__":
    main()