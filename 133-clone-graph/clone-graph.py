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
        if not node:
            return None
        visited={}
        def dfs(node):
            if node in visited :
                return visited[node]
            newnode=Node(node.val)
            visited[node]=newnode
            newnode.neighbors=[]
            for child in node.neighbors:
                newnode.neighbors.append(dfs(child))

            return newnode

        return dfs(node)


