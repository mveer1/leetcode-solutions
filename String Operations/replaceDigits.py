"""1844. Replace All Digits with Characters
You are given a 0-indexed string s that has lowercase English letters in its even indices and digits in its odd indices.

There is a function shift(c, x), where c is a character and x is a digit, that returns the xth character after c.

For example, shift('a', 5) = 'f' and shift('x', 0) = 'x'.
For every odd index i, you want to replace the digit s[i] with shift(s[i-1], s[i]).

mysol 99.4%:
"""
class Solution:
    def shift(self, char:str, x: int):
        return chr(ord(char)+x)
    
    def replaceDigits(self, s: str) -> str:
        # shift(char, x) returns xth character after char
        lis = [i for i in s]
        for i in range(1, len(lis), 2):
            lis[i] = self.shift(lis[i-1], int(lis[i]))
        return ''.join(lis)
