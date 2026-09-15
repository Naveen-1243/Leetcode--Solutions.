class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res=[]
        path=[]
        s=set()
        def dfs():
            if len(path)==len(nums):
                res.append(path.copy())
                return 
            
            for i in nums:
                if i in s:
                    continue
                path.append(i)
                s.add(i)
                dfs()

                path.pop()
                s.remove(i)
        
        dfs()
        return res