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
            add_item()
        else:
            print("Invalid choice.")
        print(MENU)
        choice = input("Enter Choice: ").upper()

    print("Thank you for using Items for hire ")
    file.close()

########

def loading_items():
    """""
    items = open("items.csv", "r")
    for line in items.readlines():
        print("! ", line.strip())
    items.close()
"""""
    items = open("items.csv", "r")
    reader = csv.reader(items, delimiter="\t")
    for i, line in enumerate(reader):
        print('{} = {}'.format(i, line))
    items.close()

#######
def hiring_item():
    return

def add_item():
    new = []

    name = input("name of item: ")
    new.append(name)
    description = input("enter description: ")
    new.append(description)
    price = input("enter price: ")
    new.append(price)
    new.append('in')
    print(new)
    add = open("items.csv", "a")
    add.write(','.join(new))
    add.close()
main()