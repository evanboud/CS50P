import random


def main():
    level = get_level()
    score = 0
    for i in range(10):
        count = 0
        x = generate_integer(level)
        y = generate_integer(level)
        while True:
            try:
                user_input = int(input(f'{x} + {y} = '))
                if user_input == x + y:
                    score = score + 1
                    break
                else:
                    print("EEE")
                    count = count + 1
                    if count == 3:
                        z = x + y
                        print(f'{x} + {y} = {z}')
                        break
                    continue
            except ValueError:
                continue
    print(f"Score: {score}")


def get_level():
    while True:
        try:
            level = input("Level: ")
            level = int(level)
            if level == 1:
                return 1
            elif level == 2:
                return 2
            elif level == 3:
                return 3
        except ValueError:
            continue


def generate_integer(level):
    if level == 1:
        x = random.randint(0, 9)
        return x
    elif level == 2:
        x = random.randint(10, 10 ** 2 - 1)
        return x
    elif level == 3:
        x = random.randint(100, 10 ** 3 - 1)
        return x

if __name__ == "__main__":
    main()
