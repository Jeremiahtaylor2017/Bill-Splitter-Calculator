# Bill Splitter Calculator
from random import choice

n_people = int(input("Enter number of people joining you (including you): "))
print()

# Establishing main dictionary where information is stored
names_dict = {}

# Logic to decide if the program should continue.
if n_people <= 0:
    print("No one is joining for the party")
else:
    print("Enter the names of everyone (including you), each on a new line.")

    # Set the initial values to 0 for the keys(names) in the dictionary
    for _ in range(n_people):
        name = input()
        names_dict[name] = 0

    print()

    bill = float(input("Enter the total bill value: "))

    split = round(bill / n_people, 2)

    # Assigns the split values to each person.
    # Total used in final output if lucky feature not used.
    names_dict = names_dict.fromkeys(names_dict, split)

    print()

    lucky_person = False

    lucky_input = input(
        "Do you want to use the \"Who's luck\" feature? Please enter Yes/No . ").strip()
    if lucky_input == "Yes":
        lucky_person = choice(list(names_dict))
        print()
        print(f'{lucky_person} is the lucky one!')
    else:
        print()
        print("No one is going to be lucky")

    # If lucky feature is used, makes sure the lucky person pays nothing and the rest split between
    # however many people there are.
    if lucky_person:
        new_split = round(bill / (n_people - 1), 2)
        for name in names_dict:
            if name == lucky_person:
                names_dict[name] = 0
            else:
                names_dict[name] = new_split

    print()
    print(names_dict)
