file = open("day6/input.txt", "r")

input_string = ""
for current_character in file:
    input_string += current_character


for current_index in range(14, len(input_string)):
    unique_characters = set(input_string[(current_index - 14) : current_index])
    if len(unique_characters) == 14:
        print(current_index)
        break
