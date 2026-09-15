class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res=[]
        s=set()
        path=[]

        def dfs():
            if len(path) == len(nums):
                res.append(path.copy())
                return 
            
            for i in range(len(nums)):
                if i in s:
                    continue
                
                if i>0 and nums[i]==nums[i-1] and i-1 not in s:
                    continue
                
                path.append(nums[i])
                s.add(i)
                dfs()

                path.pop()
                s.remove(i)
        dfs()
        return res
                