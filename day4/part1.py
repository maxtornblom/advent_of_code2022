file = open("day4/input.txt", "r")

pairs = 0
input_array = []

for x in file.readlines():
    input_array.append(x)

input_array = list(map(lambda x: x.replace("\n", ""), input_array))

for e in input_array:
    first, second = e.split(",")
    first = [int(i) for i in first.split("-")]
    second = [int(i) for i in second.split("-")]

    if first[0] <= second[0] and first[1] >= second[1]:
        pairs += 1
    elif second[0] <= first[0] and second[1] >= first[1]:
        pairs += 1

print(pairs)
