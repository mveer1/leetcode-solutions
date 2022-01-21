# Find the Duplicate Number
"""
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
There is only one repeated number in nums, return this repeated number.
"""
# mysol:
class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        dic={}
        for num in nums:
            if num in dic:
                return num
            else:
                dic[num]=0


# Approach 2: Set
class Solution:
    def findDuplicate(self, nums):
        seen = set()
        for num in nums:
            if num in seen:
                return num
            seen.add(num)


# Approach 3: Floyd's Tortoise and Hare (Cycle Detection)
class Solution:
    def findDuplicate(self, nums):
        # Find the intersection point of the two runners.
        tortoise = hare = nums[0]
        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if tortoise == hare:
                break
        
        # Find the "entrance" to the cycle.
        tortoise = nums[0]
        while tortoise != hare:
            tortoise = nums[tortoise]
            hare = nums[hare]
        
        return hare