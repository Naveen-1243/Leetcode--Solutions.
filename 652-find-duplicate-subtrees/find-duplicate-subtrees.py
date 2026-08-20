# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        
        id={}
        freq={}
        ans=[]
        def dfs(node):
            if not node:
                return 0
            
            left=dfs(node.left)
            right=dfs(node.right)

            key=(node.val, left, right)

            if key not in id:
                id[key] = len(id) + 1
            subtree = id[key]

            if subtree not in freq:
                freq[subtree] = 1
            else:
                freq[subtree] += 1
            
            if freq[subtree] == 2:
                ans.append(node)
            
            return subtree
        
        dfs(root)
        return ans