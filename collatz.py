def collatz(n):
    if n % 2 == 0:
        return (n // 2)
    else:
        return (3 * n + 1)


def main():
    try:
        number = int(input("Type any number:  "))
    except ValueError:
        print("Please provide integer")
    else:
        while collatz(number) != 1:
            print(collatz(number))
            number = collatz(number)
        print(collatz(number))


if __name__ == "__main__":
    main()
