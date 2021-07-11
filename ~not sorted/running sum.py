# running sum

"""1480. Running Sum of 1d Array
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.

mysol
"""
class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        rs = list()
        cs = 0
        for num in nums:
            cs += num
            rs.append(cs)
        return rs

class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        output = []
        output.append(nums[0])
        for i in range(1, len(nums)):
            output.append(nums[i] + output[i-1])
        return output
