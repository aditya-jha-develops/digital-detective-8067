"""Convert a base-10 integer to binary and hexadecimal."""


def main():
    try:
        number = int(input("Enter a decimal integer: "), 10)
    except ValueError:
        print("Please enter a whole number in decimal.")
        return

    print("Binary:", bin(number))
    print("Hexadecimal:", hex(number))


if __name__ == "__main__":
    main()
