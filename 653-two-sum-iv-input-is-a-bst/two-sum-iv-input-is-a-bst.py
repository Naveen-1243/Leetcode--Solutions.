# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        
        q=deque([root])
        seen={}
        while q:
            for i in range(len(q)):
                node=q.popleft()
                diff = k - node.val
                if diff in seen:
                    return True
                seen[node.val] = 1

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        
        return False








