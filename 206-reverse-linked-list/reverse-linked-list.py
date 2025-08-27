# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ori=head
        b=None
        while ori:
            a=ori
            ori=ori.next
            a.next=b
            b=a
        return b