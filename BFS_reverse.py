# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        # if root does not exist
        if root is None:
            # return empty array
            return []
        # initialize output layer
        output = []
        # initialize current layer
        curr = None
        # store root node as current layer node
        curr = [root]
        # while i have a current layer
        while curr:
            # initialize iterative layer 
            iterL = []
            # add to output layer each node values for each current nodes of the current layer
            output.append([c.val for c in curr])
            # for each node in current layer
            for node in curr:
                # check if have left node
                if node.left:
                    # append to iterative layer
                    iterL.append(node.left)
                # check if have right node
                if node.right:
                    # append to iterative layer
                    iterL.append(node.right)
            # current layer becomes iterative layer
            curr = iterL
        # return the output layer in reverse order
        return output[::-1]
        
        