class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        
        new_box=sorted(boxTypes, key=lambda x: -x[1])
        res=0
        for i in new_box:
            size,unit=i

            if truckSize >= size:
                res += size * unit
                truckSize -= size
            elif truckSize < size:
                res += truckSize*unit
                break
        return res