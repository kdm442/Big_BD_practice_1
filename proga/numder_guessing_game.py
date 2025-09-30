from colorama import init, Fore, Back, Style
init(autoreset=True)

import random

lowest_num = 1
highest_num = 100
answer = random.randint(lowest_num,highest_num)
guesses = 0
is_running = True

print(Fore.YELLOW + "Numder guessing game\n")
print(f"Select a numder between{lowest_num and {highest_num}}")

while is_running:
    guess = input("Enter your gass: ")
    
    if guess.isdigit():
        guess = int()
    guesses += 1 

    if guess < lowest_num or guess > highest_num:
        print(Fore.RED + "That numder is out on range")
        print(f"Please, select a numder between{lowest_num and {highest_num}}")
    
        
    else:
        print(Fore.RED + "Invalid guess")
        print(f"Please, select a numder between{lowest_num and {highest_num}}")
