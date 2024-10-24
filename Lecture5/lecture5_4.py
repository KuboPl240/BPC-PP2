import random

random_numbers = random.sample(range(1, 11), 3)

def get_user_input():
    user_numbers = list()
    print("Enter 3 numbers between 1 and 10:")
    
    while len(user_numbers) < 3:
        try:
            num = int(input(f"Enter number {len(user_numbers)+1}: "))
            if num < 1 or num > 10:
                raise ValueError("Number out of range! Please enter a number between 1 and 10.")
            if num in user_numbers:
                raise ValueError("Duplicate number! Please enter a unique number.")
            user_numbers.append(num)
        except ValueError as ve:
            print(ve)
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        user_numbers.append(num)
    return user_numbers

user_numbers = get_user_input()

matches = set(user_numbers).intersection(random_numbers)

print("\nGenerated Numbers:", random_numbers[:]) 
print("Your Numbers:", user_numbers)
print(f"You matched {len(matches)} number(s):", matches)

