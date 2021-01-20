# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        
        if m == n:
            return head
        
        def stack_push(s, x, last=None):
            new_head = ListNode(x)
            if last is None:
                last = new_head
            new_head.next = s
            return new_head, last
        
        
        before_rev = head
        
        for _ in range(m-2):
            before_rev = before_rev.next
        
        if m < 2:
            temp = before_rev
        else:
            temp = before_rev.next
        
        rev = None
        rev_tail = None
        for i in range(n-m+1):
            rev, rev_tail = stack_push(rev, temp.val, rev_tail)
            temp = temp.next
        
        if rev:
            before_rev.next = rev
        if rev_tail:
            rev_tail.next = temp
        
        if m < 2:
            return rev
        return head