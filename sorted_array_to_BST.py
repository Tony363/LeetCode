# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def branches(self,nums,root: TreeNode,direction):
        if isinstance(nums,int) or nums == []:
            return
        print(nums,len(nums))
        middle = nums[len(nums)//2]
        left = nums[:len(nums)//2]
        right = nums[(len(nums)//2)+1:]
        head = TreeNode(val=middle)
        if direction == "right":
            root.right = head
        elif direction == "left":
            root.left = head
        self.branches(left,head,"left")
        self.branches(right,head,"right")

        
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        """
        1) Get the Middle of the array and make it root.
        2) Recursively do same for left half and right half.
              a) Get the middle of left half and make it left child of the root
                  created in step 1.
              b) Get the middle of right half and make it right child of the
                  root created in step 1.
        """ 
        if nums == []:
            return 
        elif len(nums) == 1:
            return TreeNode(val=nums[0])
        
        middle = nums[len(nums)//2]
        left = nums[:len(nums)//2]
        right = nums[(len(nums)//2)+1:]
        head = TreeNode(val=middle)
        self.branches(left,head,"left")
        self.branches(right,head,"right")
        return head