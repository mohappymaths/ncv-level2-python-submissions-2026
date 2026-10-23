
# Function to enter marks and store them in the list
def enter_marks(marks):
    # Ask the user to enter a mark
    mark = int(input("Enter mark (-1 to stop): "))

    # Continue entering marks until the user enters -1
    while mark != -1:
        # Add the mark to the list
        marks.append(mark)

        # Ask for the next mark
        mark = int(input("Enter mark (-1 to stop): "))

    # Return the updated list of marks
    return marks


# Function to calculate the total of all marks
def calculate_total(marks):
    total = 0

    # Add each mark to the total
    for mark in marks:
        total += mark

    # Return the calculated total
    return total


# Function to calculate the average mark
def calculate_average(total, marks):
    # Divide the total by the number of marks
    return total / len(marks)


# Function to display all marks in the list
def display_marks(marks):
    # Use the index to display each mark with a number
    for x in range(len(marks)):
        print(f"{x + 1}. Mark: {marks[x]}")


# Function to display the total and average
def display_results(total, average):
    print(f"Total   : {total}")
    print(f"Average : {average:.2f}")


# Function to find and display the highest mark
def getHighest(marks):
    # Start by assuming the highest mark is 0
    highest = 0

    # Check every mark in the list
    for i in range(len(marks)):
        current = marks[i]

        # Update highest if the current mark is greater
        if current > highest:
            highest = current

    # Display the highest mark
    print(f"Highest  : {highest}")


# Function to pause the program before returning to the menu
def backToMenu():
    input("\nPress Enter to return to menu...")


# Main program
# Create an empty list to store marks
marks = []

# Initialise the menu choice
choice = 0

# Repeat the menu until the user chooses to exit
while choice != 6:
    # Display the menu options
    print("\n===== MARKS MENU =====")
    print("1. Enter marks")
    print("2. Display marks")
    print("3. Calculate total")
    print("4. Calculate average")
    print("5. Display highest mark")
    print("6. Exit")

    # Get the user's menu choice
    choice = int(input("Enter your choice: "))

    # Option 1: Enter marks
    if choice == 1:
        marks = enter_marks(marks)

    # Option 2: Display marks
    elif choice == 2:
        # Check whether marks have been entered
        if len(marks) > 0:
            display_marks(marks)
        else:
            print("No marks available.")

    # Option 3: Calculate the total
    elif choice == 3:
        if len(marks) > 0:
            total = calculate_total(marks)
            print(f"Total: {total}")
        else:
            print("Please enter marks first.")

    # Option 4: Calculate the average
    elif choice == 4:
        if len(marks) > 0:
            total = calculate_total(marks)
            average = calculate_average(total, marks)
            print(f"Average: {average:.2f}")
        else:
            print("Please enter marks first.")

    # Option 5: Display the highest mark
    elif choice == 5:
        if len(marks) > 0:
            getHighest(marks)
        else:
            print("Please enter marks first.")

    # Option 6: Exit the program
    elif choice == 6:
        print("Exiting program...")

    # Handle choices that are not on the menu
    else:
        print("Invalid choice. Try again.")

    # Pause before showing the menu again
    backToMenu()
