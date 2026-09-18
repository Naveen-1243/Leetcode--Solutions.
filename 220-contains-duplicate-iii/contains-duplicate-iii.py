from sortedcontainers import SortedList
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        
        s=SortedList()
        for i,v in enumerate(nums):
            if i > indexDiff:
                s.remove(nums[i-indexDiff-1])
            
            l=v-valueDiff
            r=v+valueDiff
            pos=s.bisect_left(l)
            if pos<len(s) and s[pos]<=r:
                return True
        
            s.add(v)
        return False

            