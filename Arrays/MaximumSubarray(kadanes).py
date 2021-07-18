# 53. Maximum Subarray
# Given an integer array nums, find the contiguous subarray 
# (containing at least one number) which has the largest sum and return its sum.


# mysol:
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        ans=[]
        ans.append(nums[0])
        for i in range(1,len(nums)):
            ans.append(max(nums[i],ans[i-1]+nums[i]))

        return max(ans)


# best:
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        """
Kadane's algorithm: At every index, see if we get better result by adding the element to the current sequence or starting a new sequence.
nums = [-2,1,-3,4,-1,2,1,-5,4]
current sequence: [-2], current sum = -2
Do we get better result by adding 1 to sequence: [-2, 1] = -1
OR do we get better result by starting sequence at 1: [1] = 1
Just take the max of those two as current sum, and update max sum as you go
        """
        curr_sum = max_sum = nums[0]
        for num in nums[1:]:
            curr_sum = max(curr_sum + num, num)
            max_sum = max(max_sum, curr_sum)
        return max_sum




import math
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        maxE = 0
        maxS = -math.inf
        
        for ele in nums:
            maxE += ele
            if maxS < maxE:
                maxS = maxE
            if maxE < 0:
                maxE = 0
        return maxS
