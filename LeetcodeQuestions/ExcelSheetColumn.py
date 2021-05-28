'''168. Excel Sheet Column Title
Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.

Input: columnNumber = 28
Output: "AB"

Input: columnNumber = 701
Output: "ZY"
'''
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        nums = range(1, 27)
        letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        
        mapp = dict(zip(nums, letters))
        
        q = 1
        n = columnNumber
        title = []
        while q > 0:
            q = n // 26
            r = n % 26
            if r == 0:
                r = 26
                q -= 1
                
            title.insert(0, mapp[r])
            n = q
        return ''.join(title)
