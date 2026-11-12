class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        
        inc=1
        dec=1

        max_inc=1
        max_dec=1

        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                inc += 1
            else:
                inc=1
            
            if nums[i]<nums[i-1]:
                dec += 1
            else:
                dec=1
            
            max_inc = max(max_inc, inc)
            max_dec = max(max_dec, dec)
        
        return max(max_inc, max_dec)