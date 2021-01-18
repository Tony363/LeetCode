# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # initialize memoization of previous node
    def __init__(self):
        self.prev = None
    # DFS traversal
    def dfs(self,root: TreeNode):
        # in order traversal
        if root is None:
            return False
        
        if self.dfs(root.left) and root.left.val == 0:
            root.left = None
        if self.dfs(root.right) and root.right.val == 0:
            root.right = None
        if root.left is None and root.right is None:
            return True
        return False
    
    def pruneTree(self, root: TreeNode) -> TreeNode:
        # check if root is None
        if root is None:
            # return
            return 
        
        # traverse left branch
        if self.dfs(root.left) and root.left.val == 0:
            root.left = None
        # traverse right branch
        if self.dfs(root.right) and root.right.val == 0:
            root.right = None
        if root.val == 0 and root.left is None and root.right is None:
            return 
        return root