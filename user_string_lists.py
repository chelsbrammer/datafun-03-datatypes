"""
Module 3, Task 4 - 1/30/23
Chelsea Brammer
Domain: Horses

"""

import random


# Define a string list
horse_names = ["Mouse", "Benny", "Yo-Yo", "Bentley", "Slack", "Soldier"]

horse_colors = ["bay", "palomino", "paint", "grulla", "sorrel", "buckskin"]

rodeo_events = ["barrel racing", "calf roping", "poles", "team roping", "calf tying"]

horse_tack = ["saddle", "halter", "breast collar", "bridle", "cinch", "sport boots"]

horse_verbs = ["walk", "trot", "canter"]
print()

divider = '--------------------------------------------------------------------------------------'
print()

print("1. Using Python Built-in Functions")

print()
print(f'The length of the horse names list is {len(horse_names)}')
print()

print(f'The unique values in the horse colors list is {set(horse_colors)}')
print()

horse_tuples = zip(horse_names, rodeo_events, horse_verbs)
print(f"Tuples of horse name, rodeo event, and verb: {list(horse_tuples)}")
print()

print(divider)
print()

print("2. Random Choice")
print()

sentence = (
    f"The horse, {random.choice(horse_names)}, that is a {random.choice(horse_colors)} "
    f"is best at {random.choice(rodeo_events)} in a {random.choice(horse_verbs)}."
)
print()
print(sentence)
print()

print(divider)
print()

print("3. Get unique words")
print()

with open("text_juliuscaesar.txt", "r") as file:
    text = file.read()
    list_words = text.split()
    unique_words = set(list_words)

unique_words_sorted = sorted(unique_words)
unique_word_count = len(unique_words_sorted)
print(f"Julius Caesar contains {unique_word_count} unique words")