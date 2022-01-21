"""3. Longest Substring Without Repeating Characters
Given a string s, find the length of the longest substring without repeating characters."""


#mysol, 9% bad.
from collections import OrderedDict
class Solution:
    def leng(self, od):
        c = 0
        for key,val in od.items():
            if val==None:
                continue
            else:
                c+=1
        return c
    def inside(self,key,od):
        if (key in od) and (od[key]!=None):
            return True
        else:
            return False
    def lengthOfLongestSubstring(self, s: str) -> int:
        od = OrderedDict()
        maxl = 0
        for i,char in enumerate(s):
            if self.inside(char,od):
                if od[char]==None:
                    continue
                index = od[char]
                for k,v in od.items():
                    if v==None:
                        continue
                    if v<=index:
                        od[k]=None
                od[char]=i
            else:
                od[char]=i
            maxl = max(maxl, self.leng(od))            
        return maxl


# best
class Solution:
    def lengthOfLongestSubstring(self, string):
        if string == "":
            return 0
        observed = {}
        chars = list(string)
        str_len = len(chars)
        left, right = 0, 0
        max_length = 0
        for right in range(str_len):
            if chars[right] in observed and observed[chars[right]] >= left:  
                max_length = max((right-left), max_length)
                left = observed[chars[right]] + 1
            observed[chars[right]] = right
        max_length = max((right-left+1), max_length)
        return max_length





class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #logic:
        #var to string candidate longest substring without repeating characters
        #var to store length of string
        #for loop to iterate through the string each character at a time
        #   if the new character was already seen, reset
        #   o/w, add the new character to the string and incr counter
        cand_counter = 0
        counter = 0
        start_idx = 0
        end_idx = 0
        mem = {} #list to remember the past seen characters
        for i in s:
            #end_idx += 1
            if i in mem:
                cand_counter = end_idx - start_idx
                if cand_counter > counter:  #update counter with the latest max val
                    counter = cand_counter 
                if mem[i] > start_idx: #update start index only if it is after the current one
                    start_idx = mem[i]  
                end_idx += 1
                mem[i] = end_idx 
            else:
                end_idx += 1
                mem[i] = end_idx
        cand_counter = end_idx - start_idx
        if cand_counter > counter:
            counter = cand_counter
        return counter




class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d, start, maxLen = {}, 0, 0
        for end, ch in enumerate(s):
            if ch in d and start <= d[ch]:
                start = d[ch] + 1
            else:
                maxLen = max(maxLen, end-start+1)
            d[ch] = end
        return maxLen