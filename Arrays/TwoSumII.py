"""Two Sum II - Input array is sorted
Given an array of integers numbers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]"""
class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        dic = dict()
        for i,number in enumerate(numbers):
            if number in dic:
                return [dic[number], i+1]
            dic[target - number] = i +1