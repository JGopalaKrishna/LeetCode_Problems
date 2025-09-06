# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head and head.next:
            temp=head.next
            head.next=head.next.next
            temp.next=head
            head=temp
        else:
            return head
        dup=head.next
        while (dup and dup.next) and dup.next.next:
            temp=dup.next
            dup.next=dup.next.next
            temp.next=temp.next.next
            dup.next.next=temp
            dup=dup.next.next
        return head