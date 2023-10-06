import random

level_1 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
level_2 = [
    *level_1, 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
    'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'y', 'x', 'z'
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
level_3 = [*level_2, '.', '!', '@', '/', '_', '-']


def main():
    while True:
        length = password_length()
        level = password_level()
        password = password_generator(length, level)
        print(f"Your password is : {password}")
        if not stop():
            break


def stop():
    while True:
        choice = input("Do you want another password yes/no : ").strip().lower()
        if choice == 'yes':
            return True
        elif choice == 'no':
            return False
        else:
            print("Wrong Input Try again")


def password_length():
    while True:
        try:
            length = int(input("Enter the length it should be more then 4 and less then 16 : "))
            if 4 <= length <= 16:
                return length
            else:
                print("Too small or to big value Try again")
        except ValueError:
            print("Only enter a number between 4 and 16 Try again")


def password_level():
    print("Level 1 has only integers")
    print("Level 2 has only alphanumeric")
    print("Level 3 has alphanumeric and some special characters")
    while True:
        try:
            level = int(input("Enter the level 1, 2 or 3 : "))
            if level in [1, 2, 3]:
                return level
            else:
                print("Wrong level Try again")
        except ValueError:
            print("Only enter a number 1, 2 or 3")


def password_generator(length, level):
    password = ""
    for i in range(length):
        if level == 1:
            password += random.choice(level_1)
        elif level == 2:
            password += random.choice(level_2)
        elif level == 3:
            password += random.choice(level_3)

    return password


if __name__ == "__main__":
    main()
