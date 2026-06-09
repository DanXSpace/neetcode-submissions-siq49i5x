# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        fast, slow = head, head
        res = 0

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        cur = slow

        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt

        first, second = head, prev

        while second:
            res = max(res, first.val + second.val)
            first = first.next
            second = second.next

        return res
