import re

names = ["Arham"]
numbers = ['03000000000']
emails = ["arhamkhan@gmail.com"]
addresses = ["Punjab, Lahore"]


def main():
    while True:
        choice = menu()
        if choice == 1:
            name = getName()
            number = getNumber()
            email = getEmail()
            address = getAddress()
            names.append(name)
            numbers.append(number)
            emails.append(email)
            addresses.append(address)
        elif choice == 2:
            delete = input("Enter name or number to delete:- ")
            if delete in names:
                index = names.index(delete)
                del names[index]
                del numbers[index]
                del emails[index]
                del addresses[index]
            elif delete in numbers:
                index = numbers.index(delete)
                del names[index]
                del numbers[index]
                del emails[index]
                del addresses[index]
            else:
                print("Input does not match any data")
        elif choice == 3:
            display()
        elif choice == 4:
            update = input("Enter name or number of the person to update")
            if update in names:
                index = names.index(update)
                names[index] = getName()
                numbers[index] = getNumber()
                emails[index] = getEmail()
                addresses[index] = getAddress()
            elif update in numbers:
                index = numbers.index(update)
                names[index] = getName()
                numbers[index] = getNumber()
                emails[index] = getEmail()
                addresses[index] = getAddress()
        elif choice == 5:
            search = input("Enter a name or a number to search:-  ")
            if search in names:
                index = names.index(search)
                print("Name    = ", names[index])
                print("Number  = ", numbers[index])
                print("Email   = ", emails[index])
                print("Address = ", addresses[index])
            elif search in numbers:
                index = numbers.index(search)
                print("Name    = ", names[index])
                print("Number  = ", numbers[index])
                print("Email   = ", emails[index])
                print("Address = ", addresses[index])
        else:
            print("Good bye")
            break


def display():
    for i in range(len(names)):
        print("\nName    = ", names[i])
        print("Number  = ", numbers[i])
        print("Email   = ", emails[i])
        print("Address = ", addresses[i])


def getName():
    name = input("Enter your name :-  ")
    return name.strip().title()


def getNumber():
    while True:
        try:
            number = input("Enter your Phone number:-  ")
            if re.search(r"^03.+", number) and len(number) == 11:
                return number
            else:
                print("Invalid Number")
        except ValueError:
            print("Enter only numbers")


def getAddress():
    address = input("Enter Address :-   ")
    return address.strip()


def getEmail():
    while True:
        email = input("Enter email :- ")
        if re.search(r"^[A-Za-z0-9_]+@[a-zA-z]+.(pk|com|edu)$", email):
            return email
        else:
            print("Invalid Email")


def menu():
    while True:
        print("\nInput 1 to add")
        print("Input 2 to delete")
        print("Input 3 to view")
        print("Input 4 to update")
        print("Input 5 to search")
        print("Input 6 to exit\n")
        try:
            choice = int(input("Input choice :- "))
            if choice in [1, 2, 3, 4, 5, 6]:
                return choice
            else:
                print("Wrong input")
        except ValueError:
            print("Wrong input")


if __name__ == "__main__":
    main()
