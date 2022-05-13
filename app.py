from datetime import date
import csv
from csv import reader

#change directory to your local csv file
data = "/Users/kaito/Desktop/Project/kakeibot/out.csv"
#today = YYYY-MM-DD
today = date.today()
year = today.strftime("%Y")
month = today.strftime("%m")
day = today.strftime("%d")

def default_message(lolist):
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n\n         Kakei BOT\n\nRespond from 1 to 3 to choose")
    print("\n 1. Input expences\n 2. Check expences\n 3. Quit bot\n")


    while True:
        try:
            start = int(input("Please select from menu: "))
        except ValueError:
            print("Sorry, I didn't understand that.")
            continue

        if start < 1 or start > 4:
            print("Sorry, your response must be 1 ~ 3.")
            continue
        else:
            break
    
    # Jumps to the add command
    if start == 1:
        addfund(lolist)
    # Jumps to the check command
    if start == 2:
        checkfund(lolist)
    # Ends the while loop
    if start == 3:
        print("\nQuitting bot\n\nUpdating Database\n\n")
        return False

    return True

    
def addfund(lolist):
    print("\nWhat did you spend money on?")
    genre = ["Food", "Gas", "Utilities", "Groceries", "Other", "Exit"]
    for i in range(len(genre)):
        print ("{}. {}".format(i+1, genre[i]))
    print("")

    while True:
        try:
            cate = int(input("Please select from menu: "))
        except ValueError:
            print("Sorry, I didn't understand that.")
            continue
        if cate < 1 or cate > 6:
            print("Sorry, your response must be 1 ~ 6.")
            continue
        if cate == 6:
            return lolist
        else:
            break

    while True:
        try:
            print("\nHow much money did you spend on {}?".format(genre[cate-1]))
            print("  Enter 0 to exit")
            cost = float(input("- "))
        except ValueError:
            print("Sorry, I didn't understand that.")
            continue
        if cost < 0:
            print("Sorry, your cost must be positive")
            continue
        if cost == 0:
            return lolist
        else:
            break
    
    print("\nYou spent ${:.2f} on {} on {}-{}-{}.".format(cost, genre[cate-1], year, month, day))
    print("  Press 1 to confirm")
    test = input("- ")
    if test == "1":
        print("\nConfirmed!, adding to database")
    else:
        print("\nConfirmation failed, returning to menu")
        return lolist
    
    #add the input to the list
    lolist.append([year, month, day, genre[cate-1], round(cost,2)])
    return lolist

def checkfund(lolist):
    total = 0.0
    print("\nWhat would you like to check?")
    allcategories = ["All", "Food", "Gas", "Utilities", "Groceries", "Other", "Exit"]
    for i in range(len(allcategories)):
        print ("{}. {}".format(i+1, allcategories[i]))
    print("")

    while True:
        try:
            cate = int(input("Please select from menu: "))
        except ValueError:
            print("Sorry, I didn't understand that.")
            continue
        if cate < 1 or cate > 7:
            print("Sorry, your response must be 1 ~ 7.")
            continue
        if cate == 7:
            return lolist
        else:
            break
    
    if cate == 1:
        for i in range(len(lolist)):
            total += float(lolist[i][4])
    
    for i in range(len(lolist)):
        if lolist[i][3] == allcategories[cate - 1]:
            total += float(lolist[i][4])

    print("\nYour total expence for {} is ${}".format(allcategories[cate - 1], total))
    return True


if __name__ == "__main__":
    user = []
    

    with open(data, "r") as read_obj:
        # pass the file object to reader() to get the reader object
        csv_reader = reader(read_obj)
        # Pass reader object to list() to get a list of lists
        user = list(csv_reader)

    while True:
        print("")
        if default_message(user) == False:
            break
    
    with open(data, "w", newline="") as f:
        writer = csv.writer(f)
        # write list of list to a csv file  
        writer.writerows(user)
    
    """
    for i in range(len(user)):
        print(user[i])
    """

    
    