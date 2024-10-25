# 9. Function to check if there are two distinct numbers in the list that add up to the target sum
def has_pair_with_sum(nums, target_sum):
    seen = set()
    for num in nums:
        if target_sum - num in seen:
            return True
        seen.add(num)
    return False

# Test for has_pair_with_sum
nums = [1, 2, 3, 4, 5]
target_sum = 9
print(has_pair_with_sum(nums, target_sum))