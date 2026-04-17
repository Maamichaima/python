import sys

NESTED_MORSE = { " ": "/ ",
                    "A": ".- ", "B": "-... ", "C": "-.-. ", "D": "-.. ", "E": ". ",
                    "F": "..-. ", "G": "--. ", "H": ".... ", "I": ".. ", "J": ".--- ",
                    "K": "-.- ", "L": ".-.. ", "M": "-- ", "N": "-. ", "O": "--- ",
                    "P": ".--. ", "Q": "--.- ", "R": ".-. ", "S": "... ", "T": "- ",
                    "U": "..- ", "V": "...- ", "W": ".-- ", "X": "-..- ", "Y": "-.-- ", "Z": "--.. ",
                    "0": "----- ", "1": ".---- ", "2": "..--- ", "3": "...-- ", "4": "....- ",
                    "5": "..... ", "6": "-.... ", "7": "--... ", "8": "---.. ", "9": "----. "}

def morse_encoder():
    if len(sys.argv) != 2:
        print("AssertionError: the arguments are bad")
        exit()
    string = sys.argv[1]
    if not all(char.isalnum() or char.isspace() for char in string):
        print("AssertionError: the arguments are bad")
        exit()
    string = string.upper()
    morse_code = ""
    for char in string:
        morse_code += NESTED_MORSE[char]
    print(f"{morse_code}")


if __name__ == "__main__":
    morse_encoder()