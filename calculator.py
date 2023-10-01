class Calculator:

    @classmethod
    def Addition(cls, num1, num2):
        return num1 + num2

    @classmethod
    def Subtraction(cls, num1, num2):
        return num1 - num2

    @classmethod
    def Multiplication(cls, num1, num2):
        return num1 * num2

    @classmethod
    def Division(cls, num1, num2):
        return num1 / num2

    @classmethod
    def Mod(cls, num1, num2):
        return num1 % num2


def main():
    calculate()


def int_Input():
    while True:
        try:
            x = float(input("What's 1st number :-  "))
            y = float(input("What's 2nd number :-  "))
            return x, y
        except ValueError:
            print("Both numbers should be an integer or float")


def menu():
    operators = ['+', '-', '*', '/', "%"]
    print("Choose an operator +,-,*,/,% :")
    while True:
        choice = input("Enter :-  ")
        if choice in operators:
            return choice
        else:
            print("Wrong Input")


def close():
    while True:
        try:
            out = input("Enter Y/y to Exit or N/n to Continue : ")
            if out in ['y', 'Y']:
                return True
            elif out in ['n', 'N']:
                return False
            else:
                raise ValueError
        except ValueError:
            print("Enter only Y/y or N/n")


def calculate():
    cal = Calculator()
    while True:
        x, y = int_Input()
        choice = menu()
        if choice == '+':
            print("Ans = ", cal.Addition(x, y))
        elif choice == '-':
            print("Ans = ", cal.Subtraction(x, y))
        elif choice == '*':
            print("Ans = ", cal.Multiplication(x, y))
        elif choice == '/':
            print("Ans = ", cal.Division(x, y))
        else:
            print("Ans = ", cal.Mod(x, y))

        if close():
            print("Goodbye")
            break


if __name__ == "__main__":
    main()
