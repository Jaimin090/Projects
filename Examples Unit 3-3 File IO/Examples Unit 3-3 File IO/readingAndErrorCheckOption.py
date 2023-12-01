def display_menu():
    print("Menu:")
    print("1. Option 1")
    print("2. Option 2")
    print("3. Option 3")

def get_user_choice():
    # this method will error check ANY user value even strings (e.g. "x")
    valid_choices = ["1", "2", "3"]
    choice = input("Enter your choice (1-3): ")
    while choice not in valid_choices:
        print("Invalid choice. Please try again.")
        choice = input("Enter your choice (1-3): ")
    return choice

# Main program
display_menu()
# the user_choise will be a string here so let's convert it to an int
user_choice = int(get_user_choice())

# Use the user_choice variable to perform the desired action
if user_choice == 1:
    print("Option 1 selected.")
    # Perform the action for option 1
elif user_choice == 2:
    print("Option 2 selected.")
    # Perform the action for option 2
elif user_choice == 3:
    print("Option 3 selected.")
    # Perform the action for option 3
