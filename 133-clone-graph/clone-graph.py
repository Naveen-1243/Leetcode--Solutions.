"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        d={}
        def dfs(node):
            if not node:
                return None
            
            if node in d:
                return d[node]
            copy=Node(node.val)
            d[node]=copy

            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy
        return dfs(node)