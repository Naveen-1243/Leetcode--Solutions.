class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        i=0
        j=0

        while i <= len(nums)-1:
            if nums[i] != 0:
                nums[i],nums[j] = nums[j],nums[i]
                i+=1
                j+=1
            elif nums[i] == 0:
                i+=1