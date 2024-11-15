while True:
    try:
        # Prompt the user for an integer input
        user_input = input("Type an integer number: ")
        
        # Attempt to convert the input to an integer
        number = int(user_input)
        
        # Break the loop if input is valid
        break
    except ValueError:
        # If input is not an integer, print an error message
        print("Incorrect value; please repeat")

# Calculate the absolute value of the entered number
absolute_value = abs(number)

# Check if the absolute value is odd or even and display the result
if absolute_value % 2 == 0:
    print(f"Absolute value {absolute_value} is even")
else:
    print(f"Absolute value {absolute_value} is odd")
