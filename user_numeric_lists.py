"""
Module 3, Task 3 - 1/29/23

Chelsea Brammer
Domain: Horses 

"""

import math
import statistics as stats

# Quickest top 20 cumulative times from the Team Roping Event with 30 total teams

team_roping_times = [30.34, 29.41, 32.19, 31.55, 30.82, 29.75, 32.26, 30.61, 30.44,
31.93, 29.62, 30.05, 32.19, 31.37, 30.08, 32.00, 29.06, 31.99, 30.01, 32.88]

# Quickest top 10 times will be in the Short-Go (aka Final Round)

x_high_call_back_times = [29.41, 29.75, 29.62, 29.06, 30.01, 30.05, 30.08, 30.34, 
30.44, 30.61]

# Each team is given a score representing their skill level
# These scores are for each high call back team

y_roper_level = [3, 3, 4, 4, 4, 5, 5, 5, 6, 6]

divider = ("----------------------------------------------------------------------------------")

print()
print("Welcome to our team roping event!")
print("We will have 30 teams total")
print("Quickest 10 teams will be in the Short-Go")
print("The 5 quickest teams will be in the money")
print("Good luck!")
print()


print("1. List Statistics")

print()
mean = stats.mean(team_roping_times)
median = stats.median(team_roping_times)
mode = stats.mode(team_roping_times)
st_dev = stats.stdev(team_roping_times)
variance = stats.variance(team_roping_times)

print(f"Team Roping Times Mean: {round(mean, 2)}")
print(f"Team Roping Times Median: {round(median,2)}")
print(f"Team Roping Times Mode: {round(mode, 2)}")
print(f"Team Roping Times Standard Deviation: {round(st_dev, 2)}")
print(f"Team Roping Times Variance: {round(variance, 2)}")
print()

print(divider)
print()

print("2. Lists - Correlation and Prediction")

print()
correlationxy = stats.correlation(x_high_call_back_times, y_roper_level)
slope, intercept = stats.linear_regression(x_high_call_back_times, y_roper_level)
futurex = 15
futurey = slope * futurex + intercept

print(f"Correlation between high call back times and roper levels: {round(correlationxy, 2)}")
print(f"Slope: {round(slope, 2)}")
print(f"Intercept: {round(intercept, 2)}")
print(f"Predicted roper score at future time: {round(futurey, 2)}")
print()

print(divider)
print()

print("3. Lists - Using Python Built-in Functions")
print()

min = min(team_roping_times)
max = max(team_roping_times)
len = len(team_roping_times)
sum = sum(team_roping_times)
avg = sum / len
set = set(team_roping_times)
sorted_times = sorted(team_roping_times)
sorted_reverse = sorted(sorted_times, reverse=True)

print(f"Minimum Team Roping Time: {min}")
print(f"Maximum Team Roping Times: {max}")
print(f"Team Roping Times Length: {len}")
print(f"Sum of Team Roping Times: {sum}")
print(f"Average of Team Roping Times: {avg} ")
print(f"Team Roping Times Set: {set}")
print(f"Team Roping Times Sorted - Ascending: {sorted_times}")
print(f"Team Roping Times Sorted - Descending: {sorted_reverse}")
print()

print(divider)
print()

print("4. List Methods")
print()

lst = [30.21, 29.76, 31.43, 29.55, 30.88, 31.15, 29.95]
print(f"Lst: {lst}")

lst.append(30.00)
print(f"Appended lst: {lst}")

lst.extend([29.03, 30.65, 31.75])
print(f'Extended List: {lst}')

lst.insert(29, 30)
print(f"Lst with Insert: {lst}")

lst.remove(30.88)
print(f"Lst with Removal: {lst}")

lst.count(29.76)
print(f"The value 29.76 appears in the list {lst.count(29.76)} times")

lst.sort()
print(f"Sorted in Ascending order: {lst}")

lst.sort(reverse=True)
print(f"Sorted in Descending order: {lst}")

lst_copy = lst.copy()
print(f"Copy of lst: {lst_copy}")

pop_first = lst.pop()
print(f"lst First Value Popped: {pop_first}")

pop_last = lst.pop(-1)
print(f"lst Last Value Popped: {pop_last}")

print()
print(divider)
print()

print("5. List Transformations - Using filter() & map()")
print()

even_times = list(filter(lambda x: x % 2 != 0, team_roping_times))
cube_times = list(map(lambda x: x ** 2, team_roping_times))
times_volume = list(map(lambda x: x * x * x, team_roping_times))

print(f"The even times from the team roping event were: {even_times}")
print(f"The cube of each time in the list were: {cube_times}")
print(f"The volume cubes were: {times_volume}")
print()

print(divider)
print()

print("6. List Transformations - Using List Comprehension")
print()

getx = [x for x in team_roping_times if x % 2 != 0]
print(f"The odd times from the team roping event are: {getx}")
print()

getx3 = [x * 3 for x in team_roping_times]
print(f"Each Team Roping time tripled: {getx3}")
print()

# Colors of horses seen at roping

colors = ['bay', 'palomino', 'grulla', 'sorrel', 'paint', 'buckskin']

colors2 = [colors.upper() for colors in colors]

print(f"The following horse colors were seen at the team roping event: {colors2}")
