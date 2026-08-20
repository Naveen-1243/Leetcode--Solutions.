# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        prev=None
        first=None
        second=None
        def dfs(node):
            nonlocal prev,first,second
            if not node:
                return 
            dfs(node.left)
            if prev and prev.val > node.val:
                if first is None:
                    first=prev
                second=node
                
            prev=node
            dfs(node.right)
            
        dfs(root)
        first.val,second.val=second.val,first.val