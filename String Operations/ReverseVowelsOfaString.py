"""345. Reverse Vowels of a String
Given a string s, reverse only all the vowels in the string and return it.
The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both cases.

Input: s = "hello"
Output: "holle"
"""

# mysol (5%)
class Solution:
    def swapinstr(self,s,i,j):
        mid = s[i+1:j]
        end = s[j+1:]
        a = s[:i]+s[j]+mid+s[i]+end
        return a
    def reverseVowels(self, s: str) -> str:
        a = s
        vowel = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        i,j = 0, len(s)-1
        while i<j:
            if not a[i] in vowel:
                i += 1
                continue
            if not a[j] in vowel:
                j -= 1
                continue
            a = self.swapinstr(a,i,j)
            i += 1
            j -= 1
        return a


# better:
class Solution:
    def reverseVowels(self, s):
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        L = list(s)
        i = 0
        j = len(L) - 1
        while i < j:
            while i < j and L[i] not in vowels:
                i += 1
            while j > i and L[j] not in vowels:
                j -= 1
            L[i], L[j] = L[j], L[i] 
            i += 1
            j -= 1
        return ''.join(L) 


# better:
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set(['A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u'])
        vowelList = []
        for c in s:
            if c in vowels:
                vowelList.append(c)
        ret = ""
        for c in s:
            if c in vowels:
                ret += (vowelList.pop())
            else:
                ret += c
        
        return ret
