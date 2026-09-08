class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        s=set(nums)
        total=0
        count=0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    total=nums[i]+nums[j]+nums[k]
                    for l in range(k+1,len(nums)):
                        if total == nums[l]:
                            count+=1
                
        return count