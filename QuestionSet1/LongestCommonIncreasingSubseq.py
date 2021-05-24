"""674. Longest Continuous Increasing Subsequence

Given an unsorted array of integers nums, return the length of the longest continuous increasing subsequence (i.e. subarray). The subsequence must be strictly increasing.

A continuous increasing subsequence is defined by two indices l and r (l < r) such that it is [nums[l], nums[l + 1], ..., nums[r - 1], nums[r]] and for each l <= i < r, nums[i] < nums[i + 1].
"""

# mysol 93%:
class Solution:
    def findLengthOfLCIS(self, nums: list[int]) -> int:
        if len(nums)<=1:
            return len(nums)
        curcis = 1
        longest = 1
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                curcis+=1
            else:
                curcis =1
            if curcis>longest:
                longest=curcis
        return longest




# official sol:
class Solution(object):
    def findLengthOfLCIS(self, nums):
        ans = anchor = 0
        for i in range(len(nums)):
            if i and nums[i-1] >= nums[i]: anchor = i
            ans = max(ans, i - anchor + 1)
        return ans