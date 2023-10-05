import sys
import re


Categories = ["JOB", "HOME", "URGENT"]
Tasks = {"JOB": [], "HOME": [], "URGENT": []}
choice = 0


def main():
    global Tasks
    category = Get_Category()
    ToDOList(category)


def Get_Category():
    global Categories
    for i, category in enumerate(Categories):
        print(f"{i + 1})  {category}")
    while True:
        c = input("Enter Category :").upper().strip()
        if c in Categories:
            return c
        else:
            print("Wrong INPUT try again")


def print_List(category):
    global Tasks
    print(f"{category} :-")
    for i, tasks in enumerate(Tasks[category]):
        print(f"{i + 1})  {tasks}")

    print("." * 3, sep="\n")


def InputAndDuplicateCheck(category):
    global Tasks
    while True:
        task = input("Task : ")
        if task in Tasks[category]:
            print("Already in the List try again")
        else:
            return task


def ToDOList(category):
    global choice
    while True:
        if choice != 4:
            print_List(category)
        print(
            "Input 1 to add task",
            "Input 2 to remove task",
            "Input 3 to change category",
            "Input 4 to see task from a category",
            "Input 5 to Exit",
            sep="\n",
        )
        while True:
            choice = int(input("INPUT :"))
            try:
                if choice in [1, 2, 3, 4, 5]:
                    break
                else:
                    print("Wrong Input")
            except ValueError:
                print("Wrong input try again")
        if choice == 1:
            task = InputAndDuplicateCheck(category)
            Tasks[category].append(task)
        elif choice == 2:
            if len(Tasks[category]) != 0:
                while True:
                    try:
                        delete = int(input("Enter Task number :"))
                        if delete < 1 or delete > len(Tasks[category]):
                            print("Invalid input too small or to big")
                        else:
                            break
                    except ValueError:
                        print("Wrong type of input enter an integer")
                del Tasks[category][delete - 1]
            else:
                print("The list is empty")
        elif choice == 3:
            main()
        elif choice == 4:
            print_List(Get_Category())
        else:
            sys.exit("Keep Working Hard")


if __name__ == "__main__":
    main()
