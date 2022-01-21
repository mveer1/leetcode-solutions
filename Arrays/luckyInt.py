""""lucky integer

1394. Find Lucky Integer in an Array
Given an array of integers arr, a lucky integer is an integer which has a frequency in the array equal to its value.

Return a lucky integer in the array. If there are multiple lucky integers return the largest of them. If there is no lucky integer return -1.

Example 2:
Input: arr = [1,2,2,3,3,3]
Output: 3
"""

# mysol 87%:
class Solution:
    def findLucky(self, arr: list[int]) -> int:
        currnum = 1
        longest = 1
        number  = 0
        longestnum = 0
        arr.sort()
        arr.append(-1)
        for i in range(1,len(arr)):
            # print("start:", arr[i],i)
            if arr[i]==arr[i-1]:
                currnum+=1
                # print("updated currnum to", currnum)
            else:
                if currnum == arr[i-1]:
                    # print("found lucky number",currnum)
                    if longestnum<currnum:
                        # print("updating longestnum")
                        longestnum= currnum
                # print("resetting currnum to 1")
                currnum =1
            if currnum>longest:
                longest=currnum
        if longestnum==0:
            return -1
        return longestnum


# other:
from collections import defaultdict

class Solution:
    def findLucky(self, arr: list[int]) -> int:
        counter_dict = defaultdict(int)
        for num in arr:
            counter_dict[num] += 1
        counter_dict[-1] = -1
        return max(num for num, frequency in counter_dict.items() if num == frequency)


# other:
from collections import defaultdict

class Solution:
    def findLucky(self, arr: list[int]) -> int:
        counts = defaultdict(int)
        for n in arr:
            counts[n] += 1
            
        luckies = [n for n in counts.keys() if counts[n]==n]
        luckies.append(-1)
        
        lucky = max(luckies)
        return lucky



# other:
from collections import Counter

class Solution:
    def findLucky(self, arr: list[int]) -> int:
        counts = Counter(arr)
        return max([k for k in counts if counts[k] == k], default=-1)

# all are good.
