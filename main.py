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
            hiring_item()
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
    items = open("items.csv", "r+")
    wr = csv.writer(items, dialect='excel')


    for line in items:
        match = line.strip().split(",")
        mylist = []

        name = match[0]
        description = match[1]
        price = match[2]
        hire = match[3]
        mylist.append((match[0], match[1], match[2], match[3]))

        for thing in mylist:
            if len(thing[3]) != 3:
                print(thing[0:3])
    items.close()
"""
            for i, lines in enumerate(mylist):
                print('{} = {}'.format(i, lines))
                i += 1


    items = open("items.csv", "r")
    reader = csv.reader(items, delimiter="\t")
    for i, line in enumerate(reader):
        print('{} = {}'.format(i, line).split())
    items.close()
"""
#######
def hiring_item():
    items = open("items.csv", "r")
    reader = csv.reader(items, delimiter="\t")
    for i, line in enumerate(reader):
        print('{} = {}'.format(i, line))
    items.close()


def add_item():
    new = []

    itemName = input("name of item: ")
    new.append(itemName)
    description = input("enter description: ")
    new.append(description)
    price = input("enter price: ")
    new.append(price)
    new.append('in')
    print(new)

    with open("output.csv", "a") as csvfile:
        wr = csv.writer(csvfile, dialect='excel')
        wr.writerow(new)

"""
    add = open("items.csv", "a")
    add.write(','.join(new))
    add.close()
"""

main()