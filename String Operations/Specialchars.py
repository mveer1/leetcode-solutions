"""We have two special characters. The first character can be represented by one bit 0. The second character can be represented by two bits (10 or 11).
Now given a string represented by several bits. Return whether the last character must be a one-bit character or not. The given string will always end with a zero.

bits = [1, 0, 0]
Output: True
Explanation: 
The only way to decode it is two-bit character and one-bit character. So the last character is one-bit character.

bits = [1, 1, 1, 0]
Output: False
Explanation: 
The only way to decode it is two-bit character and two-bit character. So the last character is NOT one-bit character.
"""
# mysol:
class Solution:
    def isOneBitCharacter(self, bits: list[int]) -> bool:
        stack = []  #will use append so the end of the list is our head
        for i in bits[:-1]:
            if i==0 and len(stack)==0:
                continue
            elif i==0 and stack[-1]==1:
                stack.remove(1)
            elif i==1 and len(stack)==0:
                stack.append(1)
            elif i==1 and stack[-1]==1:
                stack.remove(1)
        if len(stack)==1:
            return False
        return True


# Approach #1: Increment Pointer

# When reading from the i-th position, if bits[i] == 0, the next character must have 1 bit; else if bits[i] == 1, the next character must have 2 bits. We increment our read-pointer i to the start of the next character appropriately. At the end, if our pointer is at bits.length - 1, then the last character must have a size of 1 bit.

class Solution(object):
    def isOneBitCharacter(self, bits):
        i = 0
        while i < len(bits) - 1:
            i += bits[i] + 1
        return i == len(bits) - 1

# Approach #2: Greedy [Accepted]
# The second-last 0 must be the end of a character (or, the beginning of the array if it doesn't exist). Looking from that position forward, the array bits takes the form [1, 1, ..., 1, 0] where there are zero or more 1's present in total. It is easy to show that the answer is true if and only if there are an even number of ones present.

# In our algorithm, we will find the second last zero by performing a linear scan from the right. We present two slightly different approaches below.

class Solution(object):
    def isOneBitCharacter(self, bits):
        parity = bits.pop()
        while bits and bits.pop(): parity ^= 1
        return parity == 0
