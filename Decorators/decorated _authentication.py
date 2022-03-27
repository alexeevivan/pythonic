import os
import functools
from time import sleep
from colorama import init
from colorama import Fore, Back, Style

# «L.V.19 LLC» - random company name as an example
a = "A list of employees of the company «L.V.19 LLC»."
b = "Documentation related to taxation issues of the company «L.V.19 LLC»."
c = "Constituent documents (articles of association, licenses, etc.)"

welcome_message = "\nWelcome to the «About us» section."

# introductory information
menu_list_introductory = """
\n1. A list of employees of the company «L.V.19 LLC»
— — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — 
\n2. Documentation related to taxation issues of the company «L.V.19 LLC»
— — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — 
\n3. Constituent documents (articles of association, licenses, etc.)
— — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — 
"""
# information available after successful login
menu_list_main = """
\n1. A list related to the employees of the company «L.V.19 LLC»
\n\t1.1 «L.V.19 LLC» list of employees by the position
\n\t1.2 «L.V.19 LLC» employees salary list by the position
\n\t1.3 «L.V.19 LLC» employees certification results
— — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — 
\n2. Documentation related to taxation issues of the company «L.V.19 LLC»
\n\t2.1 The list of partner companies
\n\t2.2 Documentation containing information about taxes on premises owned by the company
\n\t2.3 Contact-list of inspection employees
— — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — 
\n3. Constituent documents (articles of association, licenses, etc.)
\n\t3.0.1 Will be updated soon...
— — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — 
"""

# the available user names and passwords
usernames = ["Ivan", "Julia", "Ian"]
user_1 = usernames[0]
user_2 = usernames[1]
user_3 = usernames[2]
keys = [1, 2, 3]
key_1 = keys[0]
key_2 = keys[1]
key_3 = keys[2]

print(welcome_message, Fore.MAGENTA, menu_list_introductory, Fore.WHITE)

explaining_message = "For further viewing of the information provided below, please complete the authentication procedeure."
print(explaining_message)
request_message_2 = int(input("\nPlease enter 1 to continue:"))

while request_message_2!=1:
    print(Fore.RED)
    print("An invalid response was entered. Try again or return to homepage.", Fore.WHITE)
    request_message_2 = int(input("\nPlease enter 1 to log in:"))
if request_message_2==1:
    os.system('cls' if os.name=='nt' else 'clear')


def access_to_login(func):
    def wrapper():
        sleep(1)
        os.system('cls' if os.name=='nt' else 'clear')
        print(Fore.GREEN)
        func()
        print(Fore.WHITE)
    return wrapper


@access_to_login
def login():
    print("Got it.\nUsername accepted:", username_request)


@access_to_login
def password():
    print("Got it.\nNow you are able to discover the files i have.")
    print(Fore.CYAN, menu_list_main)


username_request = str.title(input("Please enter your nickname:"))

if username_request in usernames:
    login()
    password_request = int(input("Enter a password:"))
    if password_request==keys[0] and username_request==user_1:
        password()
    elif password_request==keys[1] and username_request==user_2:
        password()
    elif password_request==keys[2] and username_request==user_3:
        password()
    else:
        os.system('cls' if os.name=='nt' else 'clear')
        print(Fore.RED)
        print("\nOops. Nice try, but it is the place with no errors in typing allowed!", Fore.WHITE)
        StopIteration
else:
    print(Fore.RED)
    print("\nOops. Nice try, but it is the place with no errors in typing allowed!", Fore.WHITE)
    StopIteration