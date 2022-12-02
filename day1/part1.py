file = open("day1/input.txt", "r")

maxi = 0
current = 0
for x in file.readlines():
    if x != "\n":
        current += int(x)
    else:
        if current > maxi:
            maxi = current

        current = 0

print(maxi)
