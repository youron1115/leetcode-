# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
            
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        print("測試")
        if head.next==None:#兩個都空的
            print("兩個都空的")
            head=None
            print("測試結束")
            return head

        s0=s()
        if s0.num_of_next(head,n)==None:#第一個就是目標，直接讓head指向第二個
            print("第一個就是目標，直接讓head指向第二個")
            print("測試結束")
            return head.next
        
        
        heads=head
        pre_node=ListNode()
        while head!=None:
            print("其他種")
            if s0.num_of_next(head,n)==None:
                #找到目標時，pre應在目標前一個，head在目標
                print("pre_node:",pre_node)
                print("head.next.next:",head.next)
                pre_node.next=head.next
                print("測試結束")
                return heads
            pre_node=head
            head=head.next
class s():               
    def num_of_next(self,node,num):
        Nth=0
        while Nth<num:
            
            node=node.next
            Nth+=1
        return node       
    