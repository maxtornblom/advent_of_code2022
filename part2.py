# A for Rock, B for Paper, and C for Scissors
# X for Rock, Y for Paper, and Z for Scissors
# 1 for Rock, 2 for Paper, and 3 for Scissors
# 0 if you lost, 3 if the round was a draw, and 6 if you won
# X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win

file = open("day2/input.txt", "r")

input_array = []
total_points = 0


points = {
    "A X": 3,
    "A Y": 4,
    "A Z": 8,
    "B X": 1,
    "B Y": 5,
    "B Z": 9,
    "C X": 2,
    "C Y": 6,
    "C Z": 7,
}

for x in file.readlines():
    input_array.append(x)

input_array = list(map(lambda x: x.replace("\n", ""), input_array))


for n in input_array:
    total_points += points[n]

print(total_points)
