# Bill Splitter Calculator
from random import choice

n_people = int(input("Enter number of people joining you (including you): "))
print()

names_dict = {}

if n_people <= 0:
    print("No one is joining for the party")
else:
    print("Enter the names of everyone (including you), each on a new line.")

    for _ in range(n_people):
        name = input()
        names_dict[name] = 0

    print()

    bill = float(input("Enter the total bill value: "))

    split = round(bill / n_people, 2)

    names_dict = names_dict.fromkeys(names_dict, split)

    print()
    # print(names_dict)

    lucky_input = input(
        "Do you want to use the \"Who's luck\" feature? Please enter y/n . ").strip()
    if lucky_input == "Yes":
        lucky_person = choice(list(names_dict))
        print()
        print(f'{lucky_person} is the lucky one!')
    else:
        print()
        print("No one is going to be lucky")
