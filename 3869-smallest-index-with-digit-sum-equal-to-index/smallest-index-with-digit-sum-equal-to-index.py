class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        
        def add(x):
            s=0
            for i in str(x):
                s+=int(i)
            return s
        
        for i in range(len(nums)):
            if add(nums[i])==i:
                return i
        return -1