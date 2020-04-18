# Initial variable to track game play
playing = "y"

# Set start and last number
number = 0
number_final = 0

# While we are still playing...
while playing == "y":

    # Ask the user how many numbers to loop through
    number_count = int(input("How many numbers? "))

    # Loop through the numbers. (Be sure to cast the string into an integer.)
    for number in range(number_count):

        # Print each number in the range
        print(number_final)
        number += 1
        number_final += 1
        
    # Set the next start number as the last number of the loop
    number = 0

    # Once complete... ask if the user wants to continue
    playing = input("Continue the chain: (y)es or (n)o? ")
