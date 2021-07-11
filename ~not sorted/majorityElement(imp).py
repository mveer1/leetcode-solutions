# *important
# 169. Majority Element
# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

# mysol: 97%
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        l = len(nums)//2
        dic = {}
        for n in nums:
            dic[n] = dic.get(n, 0) + 1
        return max(dic, key=dic.get)


# Approach 1: Brute Force

class Solution:
    def majorityElement(self, nums):
        majority_count = len(nums)//2
        for num in nums:
            count = sum(1 for elem in nums if elem == num)
            if count > majority_count:
                return num

# Algorithm
# The brute force algorithm iterates over the array, and then iterates again for each number to count its occurrences. As soon as a number is found to have appeared more than any other can possibly have appeared, return it.
# O(n^2), O(1) 


import collections
# Approach 2: HashMap

class Solution:
    def majorityElement(self, nums):
        counts = collections.Counter(nums)
        return max(counts.keys(), key=counts.get)

# O(n) O(n)



# Approach 3: 

class Solution:
    def majorityElement(self, nums):
        nums.sort()
        return nums[len(nums)//2]

# O(nlogn), O(1) or O(n) depending whether we store the array.

"""

Approach 4: Randomization

Because a given index is likely to have the majority element, we can just select a random index, check whether its value is the majority element, return if it is, and repeat if it is not. The algorithm is verifiably correct because we ensure that the randomly chosen value is the majority element before ever returning.
"""
import random

class Solution:
    def majorityElement(self, nums):
        majority_count = len(nums)//2
        while True:
            candidate = random.choice(nums)
            if sum(1 for elem in nums if elem == candidate) > majority_count:
                return candidate

"""
worst case is legit O(inf)
avg case or expected case is O(n)
O(1) for space



Approach 5: Divide and Conquer

1. Here, we apply a classical divide & conquer approach 
2. that recurses on the left and right halves of an array until an answer can be trivially achieved for a length-1 array.
3. Note that because actually passing copies of subarrays costs time and space, we instead pass lo and hi indices that describe the relevant slice of the overall array.
4. In this case, the majority element for a length-1 slice is trivially its only element, so the recursion stops there. 
5. If the current slice is longer than length-1, we must combine the answers for the slice's left and right halves. 
6. If they agree on the majority element, then the majority element for the overall slice is obviously the same. 
7. If they disagree, only one of them can be "right", so we need to count the occurrences of the left and right majority elements to determine which subslice's answer is globally correct. 
8. The overall answer for the array is thus the majority element between indices 0 and n.
"""
class Solution:
    def majorityElement(self, nums, lo=0, hi=None):
        def majority_element_rec(lo, hi):
            # base case; the only element in an array of size 1 is the majority
            # element.
            if lo == hi:
                return nums[lo]

            # recurse on left and right halves of this slice.
            mid = (hi-lo)//2 + lo
            left = majority_element_rec(lo, mid)
            right = majority_element_rec(mid+1, hi)

            # if the two halves agree on the majority element, return it.
            if left == right:
                return left

            # otherwise, count each element and return the "winner".
            left_count = sum(1 for i in range(lo, hi+1) if nums[i] == left)
            right_count = sum(1 for i in range(lo, hi+1) if nums[i] == right)

            return left if left_count > right_count else right

        return majority_element_rec(0, len(nums)-1)


"""
O(nlogn)
O(lgn)





***
Approach 6: Boyer-Moore Voting Algorithm
Intuition:
If we had some way of counting instances of the majority element as +1 and instances of any other element as -1, summing them would make it obvious that the majority element is indeed the majority element.

algorithm:
1. Essentially, what Boyer-Moore does is look for a suffix sufsuf of nums where suf[0]suf[0] is the majority element in that suffix. To do this, we maintain a count, which is incremented whenever we see an instance of our current candidate for majority element and decremented whenever we see anything else.

2. Whenever count equals 0, we effectively forget about everything in nums up to the current index and consider the current number as the candidate for majority element.

3. It is not immediately obvious why we can get away with forgetting prefixes of nums - consider the following examples (pipes are inserted to separate runs of nonzero count).

[7, 7, 5, 7, 5, 1 | 5, 7 | 5, 5, 7, 7 | 7, 7, 7, 7]

4. Here, the 7 at index 0 is selected to be the first candidate for majority element. count will eventually reach 0 after index 5 is processed, so the 5 at index 6 will be the next candidate. 

5.  In this case, 7 is the true majority element, so by disregarding this prefix, we are ignoring an equal number of majority and minority elements - therefore, 7 will still be the majority element in the suffix formed by throwing away the first prefix.

[7, 7, 5, 7, 5, 1 | 5, 7 | 5, 5, 7, 7 | 5, 5, 5, 5]

6. Now, the majority element is 5 (we changed the last run of the array from 7s to 5s), but our first candidate is still 7.

7. In this case, our candidate is not the true majority element, but we still cannot discard more majority elements than minority elements (this would imply that count could reach -1 before we reassign candidate, which is obviously false).

8. Therefore, given that it is impossible (in both cases) to discard more majority elements than minority elements, we are safe in discarding the prefix and attempting to recursively solve the majority element problem for the suffix. 

9. Eventually, a suffix will be found for which count does not hit 0, and the majority element of that suffix will necessarily be the same as the majority element of the overall array.
"""
class Solution:
    def majorityElement(self, nums):
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate

# its O(n), O(1)
