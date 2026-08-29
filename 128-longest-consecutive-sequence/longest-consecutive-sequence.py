class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        s=set(nums)
        longest=0
        for i in s:
            if i-1 not in s:
                count=1
                while i+1 in s:
                    count+=1
                    i+=1
                longest=max(longest, count)
        return longest