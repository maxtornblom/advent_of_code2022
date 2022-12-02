file = open("day1/input.txt", "r")

max_cal = 0
current_cal = 0
for x in file.readlines():
    if x != "\n":
        current_cal += int(x)
    else:
        if current_cal > max_cal:
            max_cal = current_cal

        current_cal = 0

print(max_cal)
