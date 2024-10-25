# 7. Function to remove duplicates from a list without using a set
def remove_duplicates(lst):
    unique_list = []
    for item in lst:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

# Test for remove_duplicates
lst = [1, 2, 2, 3, 4, 4, 5]
print(remove_duplicates(lst))