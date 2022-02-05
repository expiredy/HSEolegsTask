symbols_stack_count = 0

string = list(input())
initials = input()

if string[0] == "?":
    string[0] = initials[0]

for char_index in range(1, len(string)):
    if string[char_index] == initials[1] and string[char_index - 1] == initials[0]:
        symbols_stack_count += 1
    elif string[char_index] == initials[1] and string[char_index - 1] == "?":
        string[char_index - 1] = initials[0]
        symbols_stack_count += 1
    elif string[char_index] == "?" and string[char_index-1] == initials[0]:
        if char_index == len(string) - 1:
            string[char_index] = initials[1]
        else:
            string[char_index] = initials[1]
        symbols_stack_count += 1

    elif string[char_index] == "?":
        if char_index != len(string)-1:
            string[char_index] = initials[0]
        else:
            string[char_index] = initials[1]
print(symbols_stack_count)
print("".join(string))