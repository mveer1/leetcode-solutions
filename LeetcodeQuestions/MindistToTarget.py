"""1848. Minimum Distance to the Target Element
Given an integer array nums (0-indexed) and two integers target and start, find an index i such that nums[i] == target and abs(i - start) is minimized. Note that abs(x) is the absolute value of x.
Return abs(i - start).
It is guaranteed that target exists in nums.

mysol: 96%
"""
class Solution:
    def getMinDistance(self, nums: list[int], target: int, start: int) -> int:
        distance = 1
        left  = start - 1
        right = start + 1
        if nums[start] == target:
            return 0
        while left>=0 and right<len(nums):
            if nums[left]==target or nums[right]==target:
                return distance
            else:
                left -=1
                right+=1
                distance +=1
        
        indices = [i for i, x in enumerate(nums) if x == target]
        if left<0:
            return min(indices)+distance-right
        if right>=len(nums):
            return left-max(indices)+distance
