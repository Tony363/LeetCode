"""
BST Binary Search Tree
Delete one node in BST.
            ROOT                        replacement = 60
             50                              60
           /     \         delete(50)      /    \
          40      70       --------->     40     70 
         /  \    /  \                    /  \      \
       35   45  60   80                 35  45      80

 Is it safe to assume that the node to be deleted should be between the values of its children node?????

What do i replace the supposed node value to delete by?
"""

# store traversed node values in to buffer
buffer = []
# store replacement node list array 
replacement = []
# store node to delete
deleteN = None

# depth first search traversal
# val is the value i am searching for in the tree,
def DFS(root,val): 
    # first check if root is exists
    if root is None:
        # not exist return
        return
    # also check whether root node has left or children
    elif root.left is None and root.right is None:
        # if no children return
        return
    buffer = root
    # call traversal for left branch
    traversal(root.left,val)
    # call traversal for right branch
    traversal(root.right,val)
    # replace to delete node value with replacement node vlaue
    Buffer.val = min(replacement)

# method in order traversal, pre order, post order (root, val,)
def traversal(root, val):
    # check incoming root does not exist
    if root is None:
        # return to where previous node exists
        return 

    # check if current node contains to value to delete
        # assign it to deleteN

    # find node that is greater than the max node value from buffer
    if buffer.val > val:
        # append possible candidates of Node value to replace node to delete by
        replacement.append(buffer.val)
    # recursion call root.left
    traversal(root.left,val)
    # recursion call root.right
    traversal(root.right,val)
