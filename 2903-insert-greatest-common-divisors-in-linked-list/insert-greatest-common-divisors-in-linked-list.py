# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=head
        while dummy and dummy.next:
            New_Node=ListNode(math.gcd(dummy.val,dummy.next.val),dummy.next)
            dummy.next=New_Node
            dummy=dummy.next.next
        return head