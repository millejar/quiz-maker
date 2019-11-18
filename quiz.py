import xlrd
import colorama
from colorama import Fore, Back, Style
colorama.init()
import helper_functions
import sys
import random

# import the excel file
excel_file = helper_functions.import_excel()
# Open the workbook
try: 
    xl_workbook = xlrd.open_workbook(excel_file)
except: 
    print(Fore.RED + "Could not open excel file" + Fore.RESET)
    sys.exit(1)

# Retrieve and print the sheetnames
sheet_names = xl_workbook.sheet_names()
sheet_number = helper_functions.get_sheet(sheet_names)
# You can either open a sheet by name or by index
xl_sheet = xl_workbook.sheet_by_index(sheet_number)

# Test the sheet to make sure it has (at least) 4 valid columns and two valid rows. 
try:
    for col_number in range(0,4):                       # 0, 1, 2, 3
        test = xl_sheet.cell_value(1, col_number)
except:
    print(Fore.RED + "The provided sheet does not fit the required format. " +
    "Please use the template and fill in the rows with data." + Fore.RESET)
    sys.exit(1)

# Begin the quiz
print ("\n ******************************* \n")
print(Fore.CYAN + Style.BRIGHT + "Welcome to the quiz!\n" + Style.RESET_ALL)
user_continue = True
# Develop the list of available rows 
available_rows = []                      # rows that need to be quized
topics_to_work_on = []                   # rows that were not answered successfuly 
for row in range(1, xl_sheet.nrows):     # append rows of the spreadsheet to available_rows
    available_rows.append(row)

# Principal loop of the quiz
while (user_continue == True and available_rows != []): 
    print("\n ******* \n")
    # Pick a random row from available_rows, then remove it
    row_number = random.choice(available_rows)
    available_rows.remove(row_number)
    # Print the description
    helper_functions.give_description(xl_sheet.row_values(row_number))
    # Ask for the answer 
    response = helper_functions.test_user(xl_sheet.row_values(row_number), row_number, available_rows)
    available_rows = response[0]
    user_continue = response[1]
    # if user needed a hint or quit when answering the question, 
    #  add that topic back into the topics to work on 
    if (response[2]):
        for topic in response[2]:
            topics_to_work_on.append(topic)
    # If all clues have been used up, print a message indicating so 
    if (available_rows == []):
        print("\n" + Fore.CYAN + "You've answered every topic in the quiz." + Fore.RESET)

# Display the list of topics for which the user answered incorrectly or needed help
if (topics_to_work_on):
    print("\n" + Fore.LIGHTYELLOW_EX + "Here are the topics you did not answer correctly " +
    "the first time and without hints:" + Fore.RESET)
    for topic in topics_to_work_on:
        print(topic)
else:
    print(Fore.LIGHTYELLOW_EX + "You answered every topic without using any hints. Nice Work!" + Fore.RESET)

print("\n" + Fore.GREEN + "Thanks for playing!")
                
