file = open("day1/input.txt", "r")

input_array = []

current_cal = 0
for x in file.readlines():
    if x != "\n":
        current_cal += int(x)
        input_array.append(current)

    else:
        current_cal = 0

input_array.sort(reverse=True)
print(sum(input_array[:3]))
