class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if k<0:
            return 0
        d=set(nums)
        if k==0:
            return sum(nums.count(x)>1 for x in d)

        count=0
        for i in d:
            if i+k in d:
                count+=1
        return count