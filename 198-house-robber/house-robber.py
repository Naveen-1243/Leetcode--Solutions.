class Solution:
    def rob(self, nums: list[int]) -> int:
        
        if len(nums)==1:
            return nums[0]
        if len(nums)==2:
            return max(nums[0],nums[1])

        arr=[nums[0],max(nums[0],nums[1])]
        
        for i in range(2,len(nums)):
            cur=max(nums[i]+arr[i-2],arr[i-1])
            arr.append(cur)
        return arr[-1]