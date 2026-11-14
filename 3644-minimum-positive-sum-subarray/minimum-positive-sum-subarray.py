class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        ans=float('inf')
        for i in range(len(nums)):
            res=0
            length=0
            for j in range(i,len(nums)):
                res += nums[j]
                length+=1
                if l<= length <=r and 0<res<ans:
                    ans=res
         
        
        return ans if ans!=float('inf') else -1