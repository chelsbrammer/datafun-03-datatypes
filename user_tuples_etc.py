"""
Module 3, Task 5 - 1/30/23
Chelsea Brammer
Domain: Horses

"""

print()
print("TUPLES .......................................................")



# Create some tuples
horseA = ("Mouse", "Head Horse", "Grulla")
horseB = ("Benny", "Heel Horse", "Buckskin")

roping_times_A = (9.45, 10.35, 9.95, 10.15, 10.05)
roping_times_B = (9.65, 10.45, 10.00, 10.55, 10.25)

# tuple concatenation
roping_horses_times = roping_times_A + roping_times_B

# tuple repetition
ropingAThrice = roping_times_A * 3

# TODO: Start using this f-string "syntactic sugar" for quick ouptut
# just add space = space inside the curly braces
# it will print the name of the variable and the value
print(f"{horseA = }")
print(f"{horseB = }")
print(f"{roping_horses_times = }")
print(f"{ropingAThrice = }")

# tuple membership testing

roping_time10_15 = 10.15 in roping_times_A
roping_time10_55 = 10.55 in roping_times_B

print()
print("Did Mouse get a score of 10.15 at the roping today?")
print(f"10.15 was scored by Mouse: {roping_time10_15}")
print()
print("Did Benny get a score of 10.55 at the roping today?")
print(f"10.55 was scored by Benny: {roping_time10_55}")
print()


print("SETS .......................................................")

roping_levelsA = {3, 3, 4, 5, 6}
roper_levelsB = {4, 5, 6, 5, 3}

# set union
times_levels = roping_levelsA | roper_levelsB

# set intersection
times_levels_D = roping_levelsA & roper_levelsB

print()
print(f"The union of the two sets in: {times_levels}")
print()
print(f"The intersection of the two sets is: {times_levels_D}")
print()


print("DICTIONARIES .......................................................")

print()

with open("text_woodchuck.txt") as text:
    word_list = text.read().split()

word_counts_dict = {word: word_list.count(word) for word in word_list}

print(f"Word Counts in Woodchuck Text: {word_counts_dict}")
print()