# 4. Function that accepts a list of strings and returns a new list with each string reversed
def reverse_strings(strings):
    reversed_list = []
    for string in strings:
        reversed_list.append(string[::-1])
    return reversed_list

# Test for reverse_strings
strings = ["apple", "banana", "cherry"]
print(reverse_strings(strings))