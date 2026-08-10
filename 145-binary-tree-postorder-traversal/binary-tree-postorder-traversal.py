# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        res=[]
        def pre(node):
            if node is not None:
                pre(node.left)
                pre(node.right)
                res.append(node.val)
        pre(root)
        return res