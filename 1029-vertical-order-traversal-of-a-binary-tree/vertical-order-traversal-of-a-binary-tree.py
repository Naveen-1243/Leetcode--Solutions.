# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q=deque([(root, 0, 0)])
        min_col, max_col = 0, 0
        d=defaultdict(list)
        while q:
            node, column, row = q.popleft()
            min_col = min(min_col, column) 
            max_col = max(max_col, column)
            d[column].append((row, node.val))
            if node.left:
                q.append((node.left, column-1, row+1))
            if node.right:
                q.append((node.right, column+1, row+1))

        result=[]  
        for i in range(min_col, max_col+1):
            d[i].sort()
            result.append([val for row, val in d[i]])
        
        return result