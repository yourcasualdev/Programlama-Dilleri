# collatz series return how much step to reach 1
def collatz_series(number):
    number = int(number)
    if number == 1:
        return 0
    elif number % 2 == 0:
        return 1 + collatz_series(number//2)
    else:
        return 1 + collatz_series(3*number+1)


def main():

    print(collatz_series(input("")))


if __name__ == "__main__":
    main()
