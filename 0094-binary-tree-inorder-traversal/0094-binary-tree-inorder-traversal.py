# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        traversal = []

        def traverse(tree):
            # base case
            if tree is None:
                return
            traverse(tree.left)
            traversal.append(tree.val)
            traverse(tree.right)

        traverse(root)
        return traversal

            

        