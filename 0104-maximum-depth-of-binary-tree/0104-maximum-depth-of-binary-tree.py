# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        maxd = 0
        def dfs(head, depth):
            nonlocal maxd
            if head is None:
                maxd = max(maxd, depth)
                return
            dfs(head.left, depth+1)
            dfs(head.right, depth+1)
            
        dfs(root, 0)
        return maxd

