""""
similar questions to longest common increasing subsequence

1446. Consecutive Characters
Given a string s, the power of the string is the maximum length of a non-empty substring that contains only one unique character.
Return the power of the string.
 
Input: s = "abbcccddddeeeeedcba"
Output: 5
Explanation: The substring "eeeee" is of length 5 with the character 'e' only.
"""


# mysol (best ithink):
class Solution:
    def maxPower(self, s: str) -> int:
        currpower = 1
        largest = 1
        for i in range(1,len(s)):
            if s[i]==s[i-1]:
                currpower+=1
            else:
                currpower = 1
            if currpower>largest:
                largest=currpower
        return largest

# official sol:
# Approach #1: One Pass
class Solution:
    def maxPower(self, s: str) -> int:
        count = 0
        max_count = 0
        previous = None
        for c in s:
            if c == previous:
                # if same as previous one, increase the count
                count += 1
            else:
                # else, reset the count
                previous = c
                count = 1
            max_count = max(max_count, count)
        return max_count



