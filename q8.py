# 8. Function that returns keys from a dictionary where the value is greater than n
def keys_greater_than(my_dict, n):
    result = []
    for key, value in my_dict.items():
        if value > n:
            result.append(key)
    return result

# Test for keys_greater_than
my_dict = {'a': 5, 'b': 12, 'c': 3}
n = 4
print(keys_greater_than(my_dict, n))