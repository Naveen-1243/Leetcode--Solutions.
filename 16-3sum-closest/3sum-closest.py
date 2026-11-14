class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        N=len(nums)
        nums.sort()
        res=float('inf')
        for i in range(N):
            l=i+1
            r=N-1
            while l<r:
                total=nums[i]+nums[l]+nums[r]

                if abs(total-target) < abs(res-target):
                    res=total
                if total==target:
                    return total
                elif total>target:
                    r-=1
                else:
                    l+=1
        
        return res