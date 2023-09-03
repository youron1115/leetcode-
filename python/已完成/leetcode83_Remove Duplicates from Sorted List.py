# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
#解法1
"""
class Solution(object):
    def deleteDuplicates(self, head):
        
        #:type head: ListNode
        #:rtype: ListNode
        
        if head==None:
            return head

        new_node=start=head
        while new_node:
            if head.val!=new_node.val :
                head.next=new_node
                head=head.next
            new_node=new_node.next
        head.next=None
        return start
"""
#解法2
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head==None:return head
        lists=[]
        while head!=None:
            lists.append(head.val)
            head=head.next
            
        lists=sorted(lists,reverse=True)
        
        print(lists)
        start=cur=ListNode(lists[0])
        del lists[0]

        for i in lists:
            
            cur.next=ListNode(i)
            print(cur.next.val)
            cur=cur.next
            
        cur.next=None
        return start