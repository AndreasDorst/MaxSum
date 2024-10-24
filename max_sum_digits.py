import argparse
import time
import sys

def display_program_name():
    program_name = r"""

    __    __     ______     __  __     ______     __  __     __    __    
   /\ "-./  \   /\  __ \   /\_\_\_\   /\  ___\   /\ \/\ \   /\ "-./  \   
   \ \ \-./\ \  \ \  __ \  \/_/\_\/_  \ \___  \  \ \ \_\ \  \ \ \-./\ \  
    \ \_\ \ \_\  \ \_\ \_\   /\_\/\_\  \/\_____\  \ \_____\  \ \_\ \ \_\ 
     \/_/  \/_/   \/_/\/_/   \/_/\/_/   \/_____/   \/_____/   \/_/  \/_/ 
    
    """
    print(program_name)  # Print the program name
    print("This program finds the number(s) with the maximum sum of digits.\n")  # Short description

def sum_of_digits(n):
    """Calculate the sum of digits of a number."""
    return sum(int(digit) for digit in str(abs(n)))

def animated_print(text, delay=0.05):
    """Print text with a letter-by-letter animation effect."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()  # Ensure the character is printed immediately
        time.sleep(delay)   # Delay before printing the next character
    print()  # Move to the next line after the text is printed

def get_numbers(max_numbers=None, input_func=input):
    """Collect integers from the user and return them in a list."""
    max_sum = 0
    numbers_with_max_sum = []
    count = 0

    while True:
        try:
            if max_numbers and count >= max_numbers:
                animated_print("Maximum number of inputs reached.")
                break

            # Input prompt using the input_func parameter
            num = int(input_func("Enter an integer (0 to stop): "))

            if num == 0:
                break

            current_sum = sum_of_digits(num)

            # If the current sum is greater, reset the list
            if current_sum > max_sum:
                max_sum = current_sum
                numbers_with_max_sum = [num]  # Start a new list with this number
            # If the current sum matches the max, append the number
            elif current_sum == max_sum:
                numbers_with_max_sum.append(num)  # Add to the list if sum matches

            count += 1

        except ValueError:
            animated_print("Please enter a valid integer.")

    return numbers_with_max_sum, max_sum

def main(max_numbers=None):
    """Main program logic with option to continue or exit."""
    while True:
        numbers_with_max_sum, max_sum = get_numbers(max_numbers)

        if numbers_with_max_sum:
            animated_print(f"\nThe number(s) with the maximum sum of digits ({max_sum}) is/are: {', '.join(map(str, numbers_with_max_sum))}")
        else:
            animated_print("\nNo numbers were entered.")

        # Ask the user if they want to continue or exit
        while True:
            choice = input("\nWould you like to continue or exit? (yes to continue, no to exit): ").strip().lower()
            if choice in ('yes', 'y'):
                break  # Continue the outer loop to allow user to enter new numbers
            elif choice in ('no', 'n'):
                animated_print("\nExiting the program.")
                return  # Exit the function, which will stop the program
            else:
                animated_print("Invalid input. Please enter 'yes' or 'no'.")

if __name__ == "__main__":
    # Display the program name using ASCII art
    display_program_name()

    # Create an argument parser
    parser = argparse.ArgumentParser(description="A program to find the number(s) with the maximum sum of digits.")
    
    # Add optional arguments
    parser.add_argument(
        '-m', '--max', type=int, help="Maximum number of integers to input (default is unlimited)."
    )
    
    # Parse the arguments
    args = parser.parse_args()

    # Call main with optional max_numbers argument
    main(max_numbers=args.max)
