# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        temp = None
        prev = None
        while head:
            # save head next to temp
            temp = head.next
            # point head to previous node
            head.next = prev
            # assign previous node as current node
            prev = head
            # traverse head to next node
            head = temp
        head = prev
        return head