"""
Given a list [4,2,-3,1,6] Write a python program to find if there is a sub-list with sum equal to zero?
"""

def has_sublist_with_zero_sum(nums):
    cumulative_sum_set = set()
    cumulative_sum = 0
    
   
    for num in nums:
        cumulative_sum += num
        
       
        if cumulative_sum == 0 or cumulative_sum in cumulative_sum_set:
            return True
        
       
        cumulative_sum_set.add(cumulative_sum)
   
    return False


nums = [4, 2, -3, 1, 6]
result = has_sublist_with_zero_sum(nums)

if result:
    print("There is a sublist with sum equal to zero.")
else:
    print("There is no sublist with sum equal to zero.")
