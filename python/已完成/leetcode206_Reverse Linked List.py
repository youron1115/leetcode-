# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        
        true_head=head
        lists=[]
        while head:
            lists.append(head.val)
            head=head.next
        head=true_head
        while head:
            head.val=lists.pop()
            head=head.next
        return true_head
        

