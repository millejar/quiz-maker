import xlrd
import colorama
from colorama import Fore, Back, Style
colorama.init()
import helper_functions
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
    # Pick a random row from available_numbers, then remove it
    random_row = random.choice(available_numbers)
    available_numbers.remove(random_row)
    # Print the correct answer
    correct_answer = xl_sheet.cell_value(random_row, 0)
    #print("The correct answer is: ", correct_answer)
    # Print the clue
    print(Fore.CYAN + "Here is the description:" + Fore.RESET)
    print(xl_sheet.cell_value(random_row, 1))
    # Ask for the answer 
    response = helper_functions.user_answer(correct_answer, random_row, available_numbers)
    available_numbers = response[0]
    user_continue = response[1]
    # If all clues have been used up, finish the game, else ask the user if they wish to continue
    if (available_numbers == []):
        print("You've answered every clue! Congratulations!")
        break
    if (user_continue == False):
        break

print("Thanks for playing!")
                
