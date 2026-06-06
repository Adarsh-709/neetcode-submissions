# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        p, current = None, head

        while current:
            temp = current.next
            current.next = p
            p = current
            current = temp
        return p
