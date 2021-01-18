class Solution:
    def dfs(self, root):
        if root is None:
            return True, 0
        
        left_balanced, left_height = self.dfs(root.left)
        right_balanced, right_height = self.dfs(root.right)
        
        # only go deeper when left or right node has children and the difference between left and right height is no more than 1
        return left_balanced and right_balanced and abs(left_height - right_height) <= 1, max(left_height, right_height) + 1
        
    def isBalanced(self, root: TreeNode) -> bool:
        return self.dfs(root)[0]