def isperfect(num):
    num = int(num)
    sum = 0
    for i in range(1, num):
        if(num % i == 0):
            sum = sum + i
    if(sum == num):
        return "mükemmel"
    return "mükemmel değil"


def main():
    print(isperfect(input("")))


if __name__ == "__main__":
    main()
