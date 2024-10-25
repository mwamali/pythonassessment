# 6. Function to return the largest number in a tuple
def largest_in_tuple(numbers):
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest

# Test for largest_in_tuple
numbers = (10, 20, 30, 40, 50)
print(largest_in_tuple(numbers))