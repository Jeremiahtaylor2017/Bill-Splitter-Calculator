# Bill Splitter Calculator

n_people = int(input("Enter how many people joining you (including you): "))
print()

names_dict = {}

if n_people > 0:
    print("Enter the names of everyone (including you), each on a new line.")
    for i in range(n_people):
        name = input()
        names_dict[name] = 0
    print()
    print(names_dict)
else:
    print("No one is joining for the party")
