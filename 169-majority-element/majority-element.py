class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        N=len(nums)

        d={}
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        
        maxi=max(d.values())
        for k,v in d.items():
            if v == maxi:
                return k