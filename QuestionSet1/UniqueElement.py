# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
# Follow up: Could you implement a solution with a linear runtime complexity and without using extra memory?

# Input: nums = [4,1,2,1,2]
# Output: 4

# math

class List:
    pass

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return 2*sum(set(nums))-sum(nums)

# hashtable
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dic = {}
        for num in nums:
            if num in dic:
                dic[num] = 0
            else:
                dic[num] = 1        
        for k in dic:
            if dic.get(k):
                return k

# best:
# in bit manipulation
# We can XOR all bits together to find the unique number.

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = 0
        for i in nums:
            a ^= i
        return a
