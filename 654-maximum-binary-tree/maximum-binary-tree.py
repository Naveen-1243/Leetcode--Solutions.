# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        
        def dfs(left, right):

            if left > right:
                return None
            
            mid = left
            for i in range(left, right+1):
                if nums[i] > nums[mid]:
                    mid=i
            
            root=TreeNode(nums[mid])
            
            root.left = dfs(left, mid-1)
            root.right = dfs(mid+1, right)
            return root
        
        return dfs(0,len(nums)-1)