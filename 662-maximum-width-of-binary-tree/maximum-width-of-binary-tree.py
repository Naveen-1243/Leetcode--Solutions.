# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q=deque([(root,1)])
        maxi=0
        while q:
            first=q[0][1]
            for i in range(len(q)):
                node, pos = q.popleft()
                last=pos
                if node.left:
                    q.append((node.left, 2 * pos))
                if node.right:
                    q.append((node.right, 2 * pos + 1))
            
            width = last - first + 1
            maxi = max(maxi, width)
        
        return maxi