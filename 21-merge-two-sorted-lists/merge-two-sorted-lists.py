# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        new_list=ListNode()
        res=new_list
        print(res)
        while list1 or list2:
            if list1 and list2:
                if list1.val<list2.val:
                    data=list1.val
                    list1=list1.next
                else:
                    data=list2.val
                    list2=list2.next
                new_list.next=ListNode(data)
                new_list=new_list.next
            elif list1:
                new_list.next=list1
                list1=None
            elif list2:
                new_list.next=list2
                list2=None
        return res.next