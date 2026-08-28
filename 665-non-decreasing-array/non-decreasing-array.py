class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        increasing=0
        decreasing=0

        for i in range(1,len(nums)):
            if nums[i-1] > nums[i]:
                decreasing+=1
                if decreasing == 2:
                    return False
                if i==1:
                    nums[i-1] = nums[i]
                elif nums[i-2] and nums[i-2]<=nums[i]:
                    nums[i-1] = nums[i]
                elif nums[i-2] > nums[i]:
                    nums[i] = nums[i-1]
            else:
                increasing+=1
        
        return True if decreasing <= 1 else False