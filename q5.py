# 5. Function to print all keys whose values are even numbers in a dictionary
def print_even_values_keys(my_dict):
    for key, value in my_dict.items():
        if value % 2 == 0:
            print(key)

# Test for print_even_values_keys
my_dict = {'a': 2, 'b': 3, 'c': 4}
print_even_values_keys(my_dict)
