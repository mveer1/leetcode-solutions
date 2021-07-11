"""   Strings With HashMaps
      Anagram, Frequency Sort
"""

# Anagram
# T.C = O(NLOGN)
def isAnagram(s1,s2):
    print(sorted(s1))
    print(sorted(s2))
    return sorted(s1) == sorted(s2)
s1 = "SILENT"
s2 = "LISTEN"
print(isAnagram(s1,s2))


# T.C = O(N)
from collections import Counter
def isAnagram(s1,s2):
    print(Counter(s1))
    print(Counter(s2))
    return Counter(s1) == Counter(s2)
s1 = "SILENT"
s2 = "LISTEN"
print(isAnagram(s1,s2))




# Sort by Frequency
# T.C = O(NLOGN)
s = "programmingknowledge"
from collections import Counter
CT = Counter(s)
A = list(CT.items())
A.sort(key=lambda x:[x[1],x[0]])
print(A)