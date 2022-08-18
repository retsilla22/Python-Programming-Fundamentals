# create a knight
def create_knight(knights):

    # creates a new knight list
    knights_data = []

    print("Lets create a Knight!")

    # set knight info
    knights_data.append(str(input("What's the Knights name: ")))

    # add info to knight
    knights.append(knights_data)

# show and select current knight


def select_knight(knights):
    while knights_number < 1:

        print("Their name is: " + knights[0])
        knights_number += 1


# pull knight and change data
def change_data(knights):

    print("--- What would you like to update? ---")
    print("1: Knights name: " + knights[0])

    try:

        selection = int(input("Select your option"))

        if selection == 1:
            if knights_number >= 0:
                print("You have a Knight!")
            knights[0] = str(input("What is their new name: "))
            print("Your Knight's new name is: " + knights[0])
        else:
            print("--- Please select a valid option ---")

    except:
        print("--- Try Again! ---")


# This is menu selection
def menu(knight_number):

    # Print display options
    print("What do you want to do?")
    print("1: Create a new Knight")
    print("0: Exit")

    # Allows selection to be tested
    try:

        # takes the users selection option
        select = int(input("Selection Number: "))
        print()  # create a blank line

        # create a new knight
        if select == 1:
            create_knight(knights)

            # print out the knight that was made
            print("\n--- Your Knight ---\n")
            print("Knight's name: " + str(knights[knight_number][0] + "\n"))
            knights_number += 1
            menu(knights_number)

        elif select == 0:
            print("Goodbye")

        else:
            print("--- Try Again! --- \n")
            menu(knights_number)

    except:
        print("--- Try Again! ---\n")
        menu(knights_number)


# set the scene
knights_number = 0
knights = []

menu(knight_number)
