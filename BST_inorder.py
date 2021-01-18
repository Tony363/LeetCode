class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

class PostOrder:
    def __init__(self):
        self.order = []

    def traverse(self,root:TreeNode):
        # if root exists
        if root is None:
            return
        
        # if there is left children
        if root.left:
            # traverse left
            self.traverse(root.left)
        # save current root
        self.order.append(root.val)

        # then if there is root children
        if root.right:
            # traverse right
            self.traverse(root.right)

    def orderTraverse(self,root:TreeNode)->List[int]:
        # check there is tree 
        if root is None:
            return
        
        # traverse left branches
        self.traverse(root.left)

        # save head node value after traverse left branches
        self.order.append(root.val)

        # traverse right branches
        self.travers(root.right)

        # return order array
        return self.order

if __name__ == '__main__':
    root = [1,None,2,3]
