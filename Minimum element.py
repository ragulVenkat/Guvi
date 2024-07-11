"""
Write a program to find the minimum element in a rated and sorted list?
"""


def find_min_in_rotated_sorted_list(nums):
    if not nums:
        return None  
    
    left, right = 0, len(nums) - 1
    
    if nums[left] < nums[right]:
        return nums[left]
    
    while left < right:
        mid = (left + right) // 2
        
        if nums[mid] > nums[mid + 1]:
            return nums[mid + 1]
        if nums[mid] < nums[mid - 1]:
            return nums[mid]
        
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid - 1
    
    return nums[left]

rotated_sorted_list = [15, 18, 2, 3, 6, 12]
result = find_min_in_rotated_sorted_list(rotated_sorted_list)
print("The minimum element is:", result)
