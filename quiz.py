import xlrd
import colorama
from colorama import Fore, Back, Style
colorama.init()
excel_file = (r'D:\Documents\Excel Data Files\Greece.xlsx')
# Open the workbook
try: 
    xl_workbook = xlrd.open_workbook(excel_file)
except: 
    print("Could not open excel file")
# Retrieve and print the sheetnames
sheet_names = xl_workbook.sheet_names()
print('Sheet Names', sheet_names)

# You can either open a sheet by name or by index
xl_sheet = xl_workbook.sheet_by_name('Sheet1')

# Print the first column
first_column = xl_sheet.col(0)
print(xl_sheet.nrows)

import random
print ("\n ******************************* \n")
print(Fore.CYAN + Style.BRIGHT + "Welcome to the quiz!\n" + Style.RESET_ALL)
user_continue = True
# Develop the list of available rows 
available_numbers = []
for number in range(0, xl_sheet.nrows, 1):
    available_numbers.append(number)
print(available_numbers)
while (user_continue == True): 
    print("\n ******* \n")
    # Pick a random number from available_numbers, then remove it
    random_number = random.choice(available_numbers)
    available_numbers.remove(random_number)
    # Print the correct answer
    correct_answer = xl_sheet.cell_value(random_number, 0) 
    print("The correct answer is: ", correct_answer)
    print(Fore.CYAN + "Here is the description:" + Fore.RESET)
    print(xl_sheet.cell_value(random_number, 1))
    keep_guessing = True
    while (keep_guessing == True):
        while True:
            try: 
                answer = input(Fore.GREEN + "What is the answer? " + Fore.RESET)
                break
            except: 
                print(Fore.RED + "Please enter a valid response" + Fore.RESET)
                continue
        if (correct_answer.upper() == answer.upper()):
            print("That is correct")
            keep_guessing = False
        else:
            print("Sorry, that is incorrect")
            validate = False
            while (validate == False):
                try: 
                    response = input("Try Again (T) or Skip (S) ")
                except: 
                    print(Fore.RED + "Please type either T or S" + Fore.RESET)
                    continue
                if (response.upper() == "T" or response.upper() == "TRY AGAIN"):
                    validate = True
                elif (response.upper() == "S" or response.upper() == "SKIP"):
                    validate = True
                    keep_guessing = False
                    available_numbers.append(random_number)
                else:
                    print(Fore.RED + "Please Type T or S" + Fore.RESET)
    
    validate = False
    while (validate == False):
        if (available_numbers == []):
            break
        try:
            response = input("Would you like to keep going (Y/N)? ")
        except:
            print(Fore.RED + "Please type either Y or N" + Fore.RESET)
            continue
        if (response.upper() == "Y" or response.upper() == "YES"):
            validate = True
        elif (response.upper() == "N" or response.upper() == "NO"):
            validate = True
            user_continue = False
        else:
            print(Fore.RED + "Please type either Y or N" + Fore.RESET)
    
    if (available_numbers == []):
        print("You've answered every clue! Congradulations!")
        break

print("Thanks for playing!")
                
