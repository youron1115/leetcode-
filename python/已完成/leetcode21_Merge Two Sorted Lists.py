# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        print("測試")
        h=newnode=ListNode()
        while list1 and list2:
            
            if list1.val<list2.val:
                newnode.next=list1
                list1=list1.next
        
            else:
                newnode.next=list2
                list2=list2.next

            newnode=newnode.next    

        if list1:
            newnode.next=list1
        if list2:
            newnode.next=list2

        return h.next