# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # pal=None
        # dum=head
        # while dum:
        #     new_node=ListNode(dum.val)
        #     new_node.next=pal
        #     pal=new_node
        #     dum=dum.next
        # print(pal)
        # while head:
        #     if pal.val!=head.val:
        #         return False
        #     else:
        #         pal=pal.next
        #         head=head.next
        # return True
        s=""
        while head:
            s+=str(head.val)
            head=head.next
        return s==s[::-1]