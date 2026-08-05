class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        cur_subset=[]
        result=[]
        def dfs(index):
            if index==n:
                result.append(cur_subset.copy())
                return
            if index<n:
                cur_subset.append(nums[index])
                dfs(index+1)
                cur_subset.pop()
                dfs(index+1)
        dfs(0)
        return result