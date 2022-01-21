"""125. Valid Palindrome
Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

"""
# mysol:
class Solution:
    def isPalindrome(self, s: str) -> bool:
        #one way is stack, we first go to half the string, and append each char to a list. if the len is odd, we ingore the first element in second pass, (the later half pass) now, in the second half pass, we match every element. if doesnt matches or the stack is not empty by the end, its not a palindrome.  O(n)
        #Other way two pointer approach, at any time is they dont match, return False. use a while loop
        
        #slicing the string would be better than stack approch ig. 
        
        # slicing:
#         firsthalf = s[:len(s)//2]
#         laterhalf = s[len(s)//2+1:]
        
        # but we have contraints here, we consider only alphanumeric, so this wont work. and string is immutable too.
        
        # now the stack feels better approach. 
        # but lets try two pointer approch
        i=0
        j=len(s)-1
        while i<=j:
            if not s[i].isalnum():
                i +=1
                continue
            if not s[j].isalnum():
                j -=1
                continue
            if s[i].lower()==s[j].lower():
                i +=1
                j -=1
            else:
                return False
        return True
    
    
    
    #thats a correct (tested) two pointer approach   57%, though, memory better than 94% though
    # now lets check the stack approach
    
    #not working theres some problem with length/
    
#         stack = []
#         leng = 0
#         for c in s:
#             if not c.isalnum():
#                 continue
#             leng+=1
        
#         for f in s[:leng//2]:
#             if not f.isalnum():
#                 continue
#             stack.append(f)
#         print(stack)
        
#         for e in s[leng//2+1:]:
#             if not e.isalnum():
#                 continue
#             print("comparing:", e, ":with last of:", stack)
#             if e.lower() == stack[-1].lower():
#                 stack.pop()
#             else:
#                 return False
#         print(stack)
#         if not stack:
#             return True
#         return False



# best:
class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        l = len(s)
        i = 0
        j = l - 1
        if not any(map(str.isalnum, s)): return True
        while True:
            while not s[i].isalnum():
                i += 1
                #if i == l: return True
            while not s[j].isalnum():
                j -= 1
                #if j < 0: return True
            if i >= j: return True
            if not (s[i] == s[j] or s[i] == chr(ord(s[j]) ^ 32)): return False
            i += 1
            j -= 1
            
        return True
