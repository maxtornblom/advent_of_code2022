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

    first_1 = range(first[0], first[1] + 1)
    second_2 = range(second[0], second[1] + 1)

    for e in first_1:
        if e in second_2:
            pairs += 1
            break


print(pairs)
