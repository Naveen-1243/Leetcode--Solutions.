class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        start=nums[-1]
        end=-1
        
        for i in range(len(nums)-2,-1,-1):
            if nums[i]<nums[i+1]:
                end=i
                break
        if end!= -1:
            for i in range(len(nums)-1,-1,-1):
                if nums[i]>nums[end]:
                    nums[i],nums[end]=nums[end],nums[i]
                    break
        
        nums[end+1:]=reversed(nums[end+1:])
        