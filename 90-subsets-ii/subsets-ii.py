class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n=len(nums)
        res=[]
        sub=[]

        def dfs(index):
            if index==n:
                res.append(sub.copy())
                return
            if index<n:
                sub.append(nums[index])
                dfs(index+1)

                sub.pop()
                while index+1 < n and nums[index] == nums[index+1]:
                    index+=1
                dfs(index+1)
        
        dfs(0)
        return res