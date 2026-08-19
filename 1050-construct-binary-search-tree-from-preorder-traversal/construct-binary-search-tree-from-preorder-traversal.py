# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        
        if not preorder:
            return None
        
        root = TreeNode(preorder[0])
        left=[]
        right=[]
        for i in preorder[1:]:
            if i < root.val:
                left.append(i)
            else:
                right.append(i)
        
        root.left = self.bstFromPreorder(left)
        root.right = self.bstFromPreorder(right)

        return root