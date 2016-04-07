import csv

MENU = "\nMenu:\n(L)ist all items\n(H)ire an item\n(R)eturn an item\n(A)dd new item\n(Q)uit"
mylist = []

# Fuction Main runs the menu and writes the lits back to file when user quits
def main():
    print("item for hire by Kyle Hess")
    load_items()
    print(MENU)

    # items = open("items.csv", "r")
    # wr = csv.writer(items, dialect='excel')
    choice = input("Enter Choice: ").upper()
    while choice != "Q":
        if choice == "L":
            listing_items()
        elif choice == "H":
            hiring_item()
        elif choice == "R":
            return_item()
        elif choice == "A":
            add_item()
        else:
            print("Invalid choice.")
        print(MENU)
        choice = input("Enter Choice: ").upper()

    print("Thank you for using Items for hire ")
    with open("items.csv", "w", newline='') as csvfile:
        csv_out = csv.writer(csvfile, dialect='excel')
        for row in mylist:
            csv_out.writerow(row)


########
#Loads the contents of the csv file
def load_items():
    items = open("items.csv", "r")
    for line in items:
        match = line.strip().split(",")
        name = match[0]
        description = match[1]
        price = match[2]
        hire = match[3]
        mylist.append((match[0], match[1], match[2], match[3]))
    items.close()


######
#Lists the items avaliable for hire
def listing_items():
    print("* Indicates item is NOT in stock.")
    for thing in mylist:
        if thing[3] == 'out':
            print(thing,'*')
        else:
            print(thing)

#######
#Hires an item thats in and then changes it to out
def hiring_item():
    hire = str(input("Enter the Item you want to hire: "))
    for i, item_name in enumerate(mylist):
        if item_name[0] == hire:
            temp = list(mylist[i])
            temp[3] = "out"
            mylist[i] = tuple(temp)
    for thing in mylist:
        print(thing[0:])


#####
#Returns an item and changes the 'out' to 'in'
def return_item():
    hire = str(input("Enter the Item you want to Return: "))
    for i, item_name in enumerate(mylist):
        if item_name[0] == hire:
            temp = list(mylist[i])
            temp[3] = "in"
            mylist[i] = tuple(temp)
    for thing in mylist:
        print(thing[0:])


#####
#Adds a new item to the bottom of a list
def add_item():
    itemName = input("name of item: ")
    description = input("enter description: ")
    price = input("enter price: ")

    mylist.append((itemName, description, price, 'in'))

    print(mylist)

    # with open("items.csv", "a") as csvfile:
    # wr = csv.writer(csvfile, dialect='excel')
    # wr.writerow(mylist)


"""
    add = open("items.csv", "a")
    add.write(','.join(new))
    add.close()
"""
main()
