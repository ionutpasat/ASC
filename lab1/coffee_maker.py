"""
# A command-line controlled coffee maker.
"""
import time
from load_recipes import load_coffee_recipes

# Implement the coffee maker's commands. Interact with the user via stdin and print to stdout.

# Requirements:
#     - use functions
#     - use __main__ code block
#     - access and modify dicts and/or lists
#     - use at least once some string formatting (e.g. functions such as strip(), lower(),
#     format()) and types of printing (e.g. "%s %s" % tuple(["a", "b"]) prints "a b"
#     - BONUS: read the coffee recipes from a file, put the file-handling code in another module
#     and import it (see the recipes/ folder)

# There's a section in the lab with syntax and examples for each requirement.

# Feel free to define more commands, other coffee types, more resources if you'd like and have time.

# Tips:
# *  Start by showing a message to the user to enter a command, remove our initial messages
# *  Keep types of available coffees in a data structure such as a list or dict
# e.g. a dict with coffee name as a key and another dict with resource mappings (resource:percent)
# as value

# Commands
EXIT = "exit"
LIST_COFFEES = "list"
# !!! when making coffee you must first check that you have enough resources!
MAKE_COFFEE = "make"
HELP = "help"
REFILL = "refill"
RESOURCE_STATUS = "status"
commands = [EXIT, LIST_COFFEES, MAKE_COFFEE, REFILL, RESOURCE_STATUS, HELP]

# Coffee examples
ESPRESSO = "espresso"
AMERICANO = "americano"
CAPPUCCINO = "cappuccino"

# Resources examples
WATER = "water"
COFFEE = "coffee"
MILK = "milk"

# Coffee maker's resources - the values represent the fill percents
RESOURCES = {WATER: 100, COFFEE: 100, MILK: 100}

"""
Example result/interactions:

I'm a smart coffee maker
Enter command:
list
americano, cappuccino, espresso
Enter command:
status
water: 100%
coffee: 100%
milk: 100%
Enter command:
make
Which coffee?
espresso
Here's your espresso!
Enter command:
refill
Which resource? Type 'all' for refilling everything
water
water: 100%
coffee: 90%
milk: 100%
Enter command:
exit
"""

# Coffee examples
coffee_recipes = load_coffee_recipes()
coffees = list(coffee_recipes.keys())

# Print available commands
print("Bine ai venit la 5ToGo, patroane!")
print(f"Comenzi: {*commands,}")
print(f"Meniu: {*coffees,}")

def countdown(req_time):
    """Prints the time countdown"""
    while req_time:
        mins, secs = divmod(req_time, 60)
        timer = f"{mins}:{secs}"
        print(timer, end='\r')
        time.sleep(1)
        req_time -= 1

def list_coffees():
    """Prints a list of available coffees"""
    print(", ".join(coffees))


def check_resources(requested_coffee):
    """Checks if there are enough resources to make the given requested_coffee"""
    for curr_resource, curr_amount in coffee_recipes[requested_coffee].items():
        if RESOURCES[curr_resource] < curr_amount:
            print(f"Nu avem {curr_resource} pentru a-ti prepara {requested_coffee}-ul sefule")
            return False
    return True

def make_coffee(requested_coffee):
    """Makes the given requested_coffee"""
    if check_resources(requested_coffee):
        countdown(5)
        print(f"Poti ridica {requested_coffee}-ul, nasule!")
        for curr_resource, curr_amount in coffee_recipes[requested_coffee].items():
            RESOURCES[curr_resource] -= curr_amount


def refill_resource(req_resource, given_amount):
    """Refills the given resource by the given amount"""
    if req_resource == "all":
        for current_resource in RESOURCES:
            RESOURCES[current_resource] = 100
        print("A venit marfa, baroane!")
    else:
        if req_resource not in RESOURCES:
            print(f"Ce-i aia {req_resource}?")
        else:
            RESOURCES[req_resource] = min(100, RESOURCES[req_resource] + given_amount)
            print(f"{req_resource}: {RESOURCES[req_resource]}%")


if __name__ == "__main__":
    print("Ia zi veric ce-i facem?")
    while True:
        command = input().strip().lower()
        if command == EXIT:
            print("Sa traiesti, finule! Pa!")
            break
        if command == LIST_COFFEES:
            list_coffees()
        elif command == HELP:
            print("Comenzi:")
            print(", ".join(commands))
        elif command == RESOURCE_STATUS:
            for resource, amount in RESOURCES.items():
                print(f"{resource}: {amount}%")
        elif command == REFILL:
            print("Ce nu mai e? Scrie 'all' pentru a comanda tot!")
            resource = input().strip().lower()
            if resource == "all":
                refill_resource("all", 0)
            else:
                print(f"Cat {resource} sa aducem, patroane?")
                amount = int(input().strip())
                refill_resource(resource, amount)
        elif command == MAKE_COFFEE:
            print("Ia zi nasule, ce ti dau?")
            coffee = input().strip().lower()
            if coffee not in coffees:
                print(f"Ce i aia {coffee}?")
            else:
                make_coffee(coffee)
        else:
            print("Nu stiu ce e asta! Scrie 'help' sa vezi ce poti face!")
