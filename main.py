import csv

MENU = "\nMenu:\n(L)ist all items\n(H)ire an item\n(R)eturn an item\n(A)dd new item\n(Q)uit"
mylist = []


# Fuction Main runs the menu and writes the list back to file when user quits
def main():
    print("Items for hire by Kyle Hess")
    load_items()
    with open("items.csv") as f:
        print(len(f.readlines()), "Items loaded from items.csv")
    print(MENU)

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
    # tuple(mylist)
    # print(mylist)
    with open("items.csv", "w", newline='') as csvfile:
        csv_out = csv.writer(csvfile, dialect='excel')
        for row in mylist:
            csv_out.writerow(row)


########
# Loads the contents of the csv file
def load_items():
    items = open("items.csv", "r")
    # counter = 0
    for line in items:
        match = line.strip().split(",")
        name = match[0]
        description = match[1]
        price = match[2]
        hire = match[3]
        mylist.append([match[0], match[1], '$', match[3], match[4]])
        # mylist.append([counter, '=', match[0],'$' match[1], match[2], match[3]])
        # counter += 1

    items.close()


######
# Lists the items avaliable for hire
def listing_items():
    print("* Indicates item is NOT in stock.")
    for is_star in mylist:
        if is_star[4] == 'out':
            print(*is_star, '*', sep=', ')
        else:
            print(*is_star, sep=', ')


#######
##Works with the enumerate version, and no counter in load_items.
# Hires an item that is in and then changes it to 'out'.
# For it to work user has to enter Full name of item.
def hiring_item():
    hire = str(input("Enter the Item you want to hire: "))
    for i, item_name in enumerate(mylist):
        if item_name[0] == hire:
            temp = list(mylist[i])
            temp[4] = "out"
            mylist[i] = tuple(temp)
    for items in mylist:
        print(', '.join(items[0:]))


#####
# Returns an item and changes the 'out' to 'in'
def return_item():
    returning = str(input("Enter the Item you want to Return: "))
    for i, item_name in enumerate(mylist):
        if item_name[0] == returning:
            temp = list(mylist[i])
            temp[4] = "in"
            mylist[i] = tuple(temp)
    for items in mylist:
        print(', '.join(items[0:]))


#####
# Adds a new item to the bottom of a list
def add_item():
    itemName = input("Item Name: ")
    description = input("Description: ")
    price = input("Price per day: $")

    mylist.append([itemName, description, price, 'in'])
    print('{} ({}), ${} - {}'.format(itemName, description, price, "now available for hire."))
    #print(', '.join(mylist))


main()
