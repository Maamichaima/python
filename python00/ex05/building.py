import sys


def main():
    """
    Counts upper, lower, punctuation, spaces, and digits in a string.
    """
    if len(sys.argv) < 2:
        print("AssertionError: argument is missing")
        exit()
    if len(sys.argv) > 2:
        print("AssertionError: more than one argument is provided")
        exit()
    try:
        str_arg = str(sys.argv[1])
        counts = {
            "characters": len(str_arg),
            "uppercase": sum(1 for c in str_arg if c.isupper()),
            "lowercase": sum(1 for c in str_arg if c.islower()),
            "punctuation":
                sum(1 for c in str_arg if not c.isalnum() and not c.isspace()),
            "spaces": sum(1 for c in str_arg if c.isspace()),
            "digits": sum(1 for c in str_arg if c.isdigit()),
        }
        print(f"The text contains {counts['characters']} characters:")
        print(f"- {counts['uppercase']} upper letters")
        print(f"- {counts['lowercase']} lower letters")
        print(f"- {counts['punctuation']} punctuation marks")
        print(f"- {counts['spaces']} spaces")
        print(f"- {counts['digits']} digits")
    except ValueError:
        print("AssertionError: argument is not a string")
        exit()


if __name__ == "__main__":
    help(main)
    main()
