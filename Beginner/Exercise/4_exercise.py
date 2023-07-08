import random

print
choice = input("Choose One: \"rock\", \"paper\", or \"scissors\"\n").lower()

random_int = random.randint(0, 2)
computer = ["rock","paper","scissors"]

print("You chose: " + choice)
print("The computer chose: " + computer[random_int])

# if len(things) != len(set(things)):
#     print("Dups!")
#     print(set(things))
# else:
#     print("You're good.")
#     print(str(len(things)))