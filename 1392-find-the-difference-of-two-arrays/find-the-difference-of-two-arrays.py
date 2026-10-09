class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        nums1=set(nums1)
        nums2=set(nums2)
        first=[]
        second=[]

        for i in nums1:
            if i not in nums2:
                first.append(i)
        
        for i in nums2:
            if i not in nums1:
                second.append(i)
        
        res=[]
        res.append(first)
        res.append(second)
        return res