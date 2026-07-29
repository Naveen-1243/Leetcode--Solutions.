class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        
        res=[-1] * len(nums)
        stack=[]
        for i in range(len(nums)):
            while stack and nums[i] > nums[stack[-1]]:
                x=stack.pop()
                res[x]=nums[i]
            stack.append(i)
        
        for i in range(len(nums)):
            while stack and nums[i] > nums[stack[-1]]:
                x=stack.pop()
                res[x]=nums[i]
        
        return res
        
            
        