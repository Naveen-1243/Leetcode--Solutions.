class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        if len(nums1)==1:
            return True
        all_even=all(i%2==0 for i in nums1)
        all_odd=all(i%2==1 for i in nums1)

        if all_even:
            return True
        if all_odd:
            return True
        
        min_odd=float('inf')
        for i in nums1:
            if i % 2 == 1:
                min_odd=min(min_odd, i)

        for i in nums1:
            if i%2==0 and i<min_odd:
                return False
        return True