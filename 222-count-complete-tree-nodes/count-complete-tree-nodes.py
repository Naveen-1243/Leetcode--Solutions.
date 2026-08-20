# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        
        def left_side(node):
            height=0
            while node:
                height+=1
                node=node.left
            return height
        
        def right_side(node):
            height=0
            while node:
                height+=1
                node=node.right
            return height
        
        def count(node):
            if not node:
                return 0
            
            left=left_side(node)
            right=right_side(node)

            if left == right:
                return (2**left) - 1
            
            return 1 + count(node.left) + count(node.right)
        
        return count(root)