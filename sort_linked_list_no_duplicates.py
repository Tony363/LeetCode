# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        ptr = head
        prev = head
        while ptr:
            if ptr.val != prev.val:
                prev = ptr
                ptr = ptr.next
            else:
                prev.next = ptr.next
                ptr = ptr.next
        return head