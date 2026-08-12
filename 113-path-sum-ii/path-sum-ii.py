# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        result=[]
        level=[]

        def dfs(node, cur_sum):

            if not node:
                return
            
            cur_sum += node.val
            level.append(node.val)
            
            if not node.left and not node.right:
                if cur_sum == targetSum:
                    result.append(level.copy())
            else:
                dfs(node.left, cur_sum)
                dfs(node.right, cur_sum)
            level.pop()
        dfs(root, 0)
        return result