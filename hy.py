import os

wordlist = "no"
def checkwordlist():
    if os.path.exists('wordlist.txt')
        wordlist = "yes"
    else:
        wordlist = "no"
def count_numbers():
    if wordlist is "no":
        # Open the file in write mode
        with open("wordlist.txt", "w") as file:
            # Iterate through numbers from 0 to 99999999
            for number in range(100000000):
                # Convert the number to a string with 8 digits padded with leading zeros
                formatted_number = str(number).zfill(8)
                # Write the formatted number to the file
                file.write(formatted_number + "\n")
    else:
        print("wordlist already exist")
checkwordlist()
# Call the function to count and save the numbers
count_numbers()
