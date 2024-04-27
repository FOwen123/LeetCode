# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Breadth First Search
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:  
            return 0

        queue = [(root, 1)]
        ans = 0

        while queue:
            root, nums = queue.pop()

            if not root.left and not root.right:
                ans = max(ans, nums)

            if root.left:
                queue.append((root.left, nums + 1))
            
            if root.right:
                queue.append((root.right, nums + 1))

        return ans

            
