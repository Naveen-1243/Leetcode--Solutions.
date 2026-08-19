# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        if not root:
            return 0
        
        count=0
        def path(node, t):
            if not node:
                return 0
            nonlocal count
            t += node.val

            
            if t == targetSum:
                count+=1
                
            
            path(node.left, t)
            path(node.right, t)
            
            return count

        count += self.pathSum(root.left, targetSum)
        path(root, 0)
        count += self.pathSum(root.right, targetSum)

        return count
        