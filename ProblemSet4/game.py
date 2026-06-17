import random

# input for level
def main():
    while True:
        try:
            level = input("Level: ")
            level = int(level)
            level_valid = level > 0
            if level_valid:
                while True:
                    try:
                        rand = random.randint(1, level)
                        Guess = input("Guess: ")
                        Guess = int(Guess)
                        Guess_Valid = Guess > 0
                        if Guess_Valid:
                            if Guess > rand:
                                print("Too Large!")
                            elif Guess < rand:
                                print("Too Small!")
                            elif Guess == rand:
                                print("Just Right!")
                                return
                            else:
                                continue
                        else:
                            continue
                    except ValueError:
                        continue
        except ValueError:
            continue

main()


#input for integer n

#randomly generate between 1 and n (inclusive

#Prompts the user to guess if not positive should prompt again