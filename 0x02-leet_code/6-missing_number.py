"""
Given an array nums containing n distinct numbers in
the range [0,  n], return the only number in the range
that is missing from the list. 
"""

def missing_number(nums):
    return sum(range(len(nums)+1)) - sum(nums)

nums1 = [3, 0, 1]
print(missing_number(nums1))
nums2 = [0, 1]
print(missing_number(nums2))
nums3 = [9,6,4,2,3,5,7,0,1]
print(missing_number(nums3))