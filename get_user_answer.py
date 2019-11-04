import colorama
from colorama import Fore, Back, Style
colorama.init()

def user_answer(correct_answer, random_number, available_numbers):
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
    return available_numbers