import csv

MENU = "\nMenu:\n(L)ist all items\n(H)ire an item\n(R)eturn an item\n(A)dd new item\n(Q)uit"

def main():
    print("item for hire by Kyle Hess")
    print(MENU)

    file = open("items.csv", "r")

    choice = input("Enter Choice: ").upper()
    while choice != "Q":

        if choice == "L":
            loading_items()
        elif choice == "H":
            print("Hire an Item")
        elif choice == "R":
            print("return item")
        elif choice == "A":
            print("add an item")
        else:
            print("Invalid choice.")
        print(MENU)
        choice = input("Enter Choice: ").upper()

    print("Thank you for using Items for hire ")
    file.close()

########

def loading_items():
    items = open("items.csv", "r")
    for line in items.readlines():
        print("! ", line.strip())
    items.close()


#######
def hiring_item():
    return


main()