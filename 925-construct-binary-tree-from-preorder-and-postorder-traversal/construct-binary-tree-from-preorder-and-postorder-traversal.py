# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        
        if len(preorder) == 1:
            return TreeNode(preorder[0])

        root = TreeNode(preorder[0])
        mid=postorder.index(preorder[1])
        
        root.left=self.constructFromPrePost(preorder[1:mid+2], postorder[:mid+1])
        root.right=self.constructFromPrePost(preorder[mid+2:], postorder[mid+1:-1])

        return root