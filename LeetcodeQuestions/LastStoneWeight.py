'''LastStoneWeight.py
We have a collection of stones, each stone has a positive integer weight.

Each turn, we choose the two heaviest stones and smash them together.  Suppose the stones have weights x and y with x <= y.  The result of this smash is:

If x == y, both stones are totally destroyed;
If x != y, the stone of weight x is totally destroyed, and the stone of weight y has new weight y-x.
At the end, there is at most 1 stone left.  Return the weight of this stone (or 0 if there are no stones left.)
'''

class Solution(object):
    def lastStoneWeight(self, stones):
        stones.sort()
        while stones:
            biggest = stones.pop()
            if not stones:
                return biggest
            second = stones.pop()
            if biggest != second:
                stones.append(biggest - second)
                stones.sort()
        
        return 0

#mysol: 
class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        for i in range(1,len(stones)):
            one = max(stones)
            stones.remove(one)
            other = max(stones)
            stones.remove(other)
            stones.append(one-other)
            
        return stones[0]
