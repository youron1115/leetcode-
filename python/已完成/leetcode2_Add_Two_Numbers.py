#Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        total=0
        carry=0
        lists=[]
        

        while l1!=None and l2!=None:
            total=l1.val+l2.val+carry
            carry=total//10
            total=total%10
            lists.insert(0,total)
            l1=l1.next
            l2=l2.next
        print(lists)
        while l1!=None and l2==None:
            total=l1.val+carry
            carry=total//10
            total=total%10
            lists.insert(0,total)
            l1=l1.next
        print(lists)
        while l1==None and l2!=None:
            total=l2.val+carry
            carry=total//10
            total=total%10
            lists.insert(0,total)
            l2=l2.next
        print(lists)
        while l1==None and l2==None and carry!=0:
            lists.insert(0,carry)
            carry=0
        print(lists)
        print("測試結束")
        return_node=ListNode(lists[0])
        del lists[0]

        for i in lists:
            return_node=ListNode(i,return_node)
            
        return return_node
        """
        """