# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode | None) -> int:
        
        res=0
        n=[root]
        while n:
            node=n.pop()
            if node.left:
                if not node.left.left and not node.left.right:
                    res += node.left.val
                else:
                    n.append(node.left)
            
            if node.right:
                n.append(node.right)
        
        return res