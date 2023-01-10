file = open("day5/input.txt", "r")

input_array = []

for x in file.readlines():
    input_array.append(x)

input_array = list(map(lambda x: x.replace("\n", ""), input_array))

stacks = input_array[:8]

stack_1 = []
stack_2 = []
stack_3 = []
stack_4 = []
stack_5 = []
stack_6 = []
stack_7 = []
stack_8 = []
stack_9 = []

for line in stacks:
    if line.find("[", 0, 1) > -1:
        stack_1.append(line[1])

    if line.find("[", 4, 5) > -1:
        stack_2.append(line[5])

    if line.find("[", 8, 9) > -1:
        stack_3.append(line[9])

    if line.find("[", 12, 13) > -1:
        stack_4.append(line[13])

    if line.find("[", 16, 17) > -1:
        stack_5.append(line[17])

    if line.find("[", 20, 21) > -1:
        stack_6.append(line[21])

    if line.find("[", 24, 25) > -1:
        stack_7.append(line[25])

    if line.find("[", 28, 29) > -1:
        stack_8.append(line[29])

    if line.find("[", 32, 33) > -1:
        stack_9.append(line[33])


stacks = [
    stack_1,
    stack_2,
    stack_3,
    stack_4,
    stack_5,
    stack_6,
    stack_7,
    stack_8,
    stack_9,
]
for command in input_array[10:]:
    numbers = command.replace("move", "").replace("from", "").replace("to", "").split()
    amount = int(numbers[0])
    source = int(numbers[1]) - 1
    destination = int(numbers[2]) - 1

    for x in range(amount):
        element = stacks[source].pop(amount - 1 - x)
        stacks[destination].insert(0, element)

result = ""
for stack in stacks:
    result += stack[0]

print(result)
