def count_numbers():
    # Open the file in write mode
    with open("pass.txt", "w") as file:
        # Iterate through numbers from 0 to 99999999
        for number in range(100000000):
            # Convert the number to a string with 8 digits padded with leading zeros
            formatted_number = str(number).zfill(8)

            # Write the formatted number to the file
            file.write(formatted_number + "\n")

    print("Numbers counted and saved to pass.txt")

# Call the function to count and save the numbers
count_numbers()