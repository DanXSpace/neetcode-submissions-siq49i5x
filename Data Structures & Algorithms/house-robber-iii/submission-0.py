# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node):
            if not node:
                return (0, 0)
            
            left_with, left_without = dfs(node.left)
            right_with, right_without = dfs(node.right)

            # choice a: rob the house
            rob_this = node.val + left_without + right_without

            # choice b: skip this house
            skip_this = max(left_with, left_without) + max(right_with, right_without)

            return (rob_this, skip_this)
            
        root_with, root_without = dfs(root)
        return max(root_with, root_without)