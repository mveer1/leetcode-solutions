# 1832. Check if the Sentence Is Pangram

# mysol:
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        sett = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'}
        for s in sentence:
            try:
                sett.remove(s)
            except:
                pass
            
        if len(sett)==0:
            return True
        else:
            return False

"""similar but simple:
comp = set()
for i in sentence:
   comp.add(i)
        
if len(comp) == 26:
    return True
    
return False
"""