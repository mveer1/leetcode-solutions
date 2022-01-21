"""1710. Maximum Units on a Truck
Easy
You are assigned to put some amount of boxes onto one truck. You are given a 2D array boxTypes, where boxTypes[i] = [numberOfBoxesi, numberOfUnitsPerBoxi]:
You are also given an integer truckSize, which is the maximum number of boxes that can be put on the truck. You can choose any boxes to put on the truck as long as the number of boxes does not exceed truckSize.
Return the maximum total number of units that can be put on the truck.
"""
# mysol:
class Solution:
    def maximumUnits(self, boxTypes: list[list[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        size,i,result = 0,0,0
        while (size < truckSize and i<len(boxTypes)):
            numbox = boxTypes[i][0]
            if (size+numbox)>truckSize:
                numbox = truckSize - size
            result = result + boxTypes[i][1]*numbox
            size += boxTypes[i][0]
            print(i,size)
            i += 1
        return result

# better sol:
class Solution:
    def maximumUnits(self, boxTypes: list[list[int]], truckSize: int) -> int:
        box_dict = {}
        for num, unit in boxTypes:
            if unit not in box_dict.keys():
                box_dict[unit] = num
            else:
                box_dict[unit] += num
                
        total_num = 0
        result = 0
        for unit in sorted(box_dict.keys(), reverse=True):
            if total_num + box_dict[unit] > truckSize:
                result += (truckSize - total_num) * unit
                return result
            
            result += unit * box_dict[unit]
            total_num += box_dict[unit]    
        else:
            return result