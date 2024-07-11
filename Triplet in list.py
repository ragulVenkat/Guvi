"""
You have been given a Python list [10, 20, 30, 9] and a value of 59. Write a python program to find the triplet in the list whose sum is equal to the given value
"""


def find_triplet_with_sum(nums, target):
  
    nums.sort()
    n = len(nums)
    triplets = []
    
    for i in range(n - 2):
        left = i + 1
        right = n - 1
        
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            if current_sum == target:
                triplets.append((nums[i], nums[left], nums[right]))
                left += 1
                right -= 1
            elif current_sum < target:
                left += 1
            else:
                right -= 1
    
    return triplets


nums = [10, 20, 30, 9]
target = 59
triplets = find_triplet_with_sum(nums, target)

if triplets:
    print("Triplets with sum", target, ":", triplets)
else:
    print("No triplet found with sum", target)
