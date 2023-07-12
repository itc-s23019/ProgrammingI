import random


def main():
    name = "KIICHI"
    a = name[0].upper()

    while True:
        i = chr(random.randint(65, 90))
        print(i)

        if i == a:
            break


if __name__ == "__main__":
    main()
