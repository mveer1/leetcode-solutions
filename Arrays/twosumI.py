
"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""
import collections
# Hashtable: One-pass, Make with Find
class solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)
        dic = collections.defaultdict(int)
        # O(N)
        for i in range(n):
            complement = target - nums[i]
            if complement in dic:
                return [i, dic[complement]]
            dic[nums[i]] = i


    # Hashtable: Two-pass, Make and Find
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)
        dic = collections.defaultdict(int)
        # O(N)
        for idx, num in enumerate(nums):
            dic[num] = idx
        
        # O(N)
        for i in range(n):
            complement = target - nums[i]
            if complement in dic:
                if i != dic[complement]:
                    return [i, dic[complement]]
        
    # Brute force, Loop through each element x
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]