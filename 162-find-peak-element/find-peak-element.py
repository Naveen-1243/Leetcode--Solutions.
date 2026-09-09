class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        peak_val=0
        peak=False
        peak_index=0
        for i in range(len(nums)-1):
            if nums[i]>nums[i+1]:
                if nums[i] >= peak_val:
                    peak_val=nums[i]
                    peak_index=i
                    peak=True
        
        if peak == True:
            return peak_index
        else:
            if nums[0]>nums[-1]:
                return 0
            return len(nums)-1