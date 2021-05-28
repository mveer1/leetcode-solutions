"""Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"
"""

# my solution:  32ms
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if len(strs)<1:
            return ""
        if len(strs)==1:
            return strs[0]
        for i,char in enumerate(strs[0]):
            for s in strs:
                try:
                    if char != s[i]:
                        return s[:i]
                except:
                    return s[:i]
        return strs[0]


    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""
        
        strs.sort()
        
        result = []
        
        for idx, char in enumerate(strs[0]):
            if char == strs[-1][idx]:
                result.append(char)
            else:
                break
        
        return "".join(result)

# https://leetcode.com/problems/longest-common-prefix/solution/
# 4 official solutions