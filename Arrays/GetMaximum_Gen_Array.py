"""Get Maximum in Generated Array

You are given an integer n. An array nums of length n + 1 is generated in the following way:

nums[0] = 0
nums[1] = 1
nums[2 * i] = nums[i] when 2 <= 2 * i <= n
nums[2 * i + 1] = nums[i] + nums[i + 1] when 2 <= 2 * i + 1 <= n
Return the maximum integer in the array nums​​​.

Input: n = 3
Output: 2
Explanation: According to the given rules, the maximum between nums[0], nums[1], nums[2], and nums[3] is 2.
"""

# mysol:
class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        nums = [0]*(n+1)
        if n<=1:
            return n
        nums[0] = 0
        nums[1] = 1
        largest = -1
        even = n//2+1
        if n%2==0:
            even = n//2
        for i in range(even):
            nums[2*i] = nums[i]
            nums[2*i+1] = nums[i]+nums[i+1]
            if nums[2*i]>nums[2*i+1]:
                large = nums[2*i]
            else:
                large = nums[2*i+1]
            if large>largest:
                largest=large
        return largest

# best:
class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        arr = []
        cur_max = 0
        for i in range(n + 1):
            if i == 0 or i == 1:
                arr.append(i)
            elif i % 2 == 0:
                arr.append(arr[i // 2])
            else:
                arr.append(arr[i // 2] + arr[i // 2 + 1])
            if arr[i] > cur_max:
                cur_max = arr[i]
        return cur_max