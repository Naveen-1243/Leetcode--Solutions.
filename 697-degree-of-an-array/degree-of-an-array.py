class Solution:
    def findShortestSubArray(self, nums: list[int]) -> int:
        
        d={}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        
        maxi=max(d.values())
        ans=len(nums)
        for k,v in d.items():
            if maxi==v:
        
                for i in range(len(nums)):
                    if nums[i]==k:
                        x=i
                        break
                
                for i in range(len(nums)-1,-1,-1):
                    if nums[i]==k:
                        y=i
                        break
                ans=min(ans, y-x+1)
                
        return ans