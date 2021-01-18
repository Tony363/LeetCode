class Solution(object):
    def isSymmetric(self, root):
        if not root: return True
        return self.checkSymmetric(root, root)
        
    def checkSymmetric(self, node1, node2):
        if not node1 and not node2: return True
        if not node1 or not node2: return False
        if node1.val != node2.val: return False
        return self.checkSymmetric(node1.left, node2.right) and self.checkSymmetric(node1.right, node2.left)