"""Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
"""
def searchInsert(self, nums: list[int], target: int) -> int:
        if target <= nums[0]:
            return 0
        if target > nums[-1]:
            return len(nums)
        for i in range(1, len(nums)):
            if nums[i] == target:
                return i
            if nums[i-1] < target < nums[i]:
                return i


# Mysolution: 52ms
class Solution:   
 def searchInsert(self, nums: list[int], target: int) -> int:
        for i,num in enumerate(nums):
            if target<=num:
                return i
        return len(nums)
