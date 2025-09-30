from colorama import init, Fore, Back, Style
init(autoreset=True)


menu = {"potato_free" : 6.00,
        "popcorn" : 14.00,
        "coke" : 7.50,
        "beer" : 16.75,
        "hotdog" : 15.50,
        "icecream" : 18.00,
        "chips" : 10.00}

cart = []
total = 0

print(Fore.GREEN +"------------Menu--------------\n")
for key, value in menu.items():
    print(f"{key:15}: {value:.2f}$")
print(Fore.GREEN +"------------------------------\n")

while True:
    food = input("Select to items in menu (q to quit): ").lower()
    if food == "q":
        break
    if menu.get(food) is not None:
        cart.append(food)
        print(Fore.GREEN + f"{food} in cart!")
    else:
        print(Fore.RED + "This food is non on menu")

print(Fore.GREEN + "---------YOUR ORDER-----------")
for food in cart:
    total += menu.get(food)

    
print(f"Your cart: {cart}")
print(Fore.GREEN + f"Price: {total}$")        
    