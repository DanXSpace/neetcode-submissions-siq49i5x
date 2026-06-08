# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def backtracking(node, pathSum):
            if not node:
                return False
                
            pathSum += int(node.val)

            if node.left is None and node.right is None:
                return pathSum == targetSum
            
            if backtracking(node.left, pathSum):
                return True
            if backtracking(node.right, pathSum):
                return True
            
            return False
        return backtracking(root, 0)