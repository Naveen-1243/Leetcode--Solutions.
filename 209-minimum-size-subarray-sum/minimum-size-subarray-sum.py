class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        left=0
        cur_sum=0
        mini=float('inf')
        for right in range(len(nums)):
            cur_sum+=nums[right]
            while cur_sum >= target:
                mini=min(mini,right-left+1)
                cur_sum-=nums[left]
                left+=1
        return 0 if mini==float('inf') else mini