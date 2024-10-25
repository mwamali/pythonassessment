# 10. Function that takes a list of tuples and returns a dictionary
def tuples_to_dict(tuples_list):
    result_dict = {}
    for key, value in tuples_list:
        result_dict[key] = value
    return result_dict

# Test for tuples_to_dict
tuples_list = [("apple", 5), ("banana", 3), ("cherry", 7)]
print(tuples_to_dict(tuples_list))