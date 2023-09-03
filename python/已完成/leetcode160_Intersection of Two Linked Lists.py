# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        
        """
        Given the heads of two singly linked-lists headA and headB, 
        return the node at which the two lists intersect(此指位置相同之開始處). 
        If the two linked lists have no intersection at all, 
        return null.
        """
        if headA is None or headB is None:
            return None
        a=[]
        b=[]
        
        while headA or headB:
            if headA:
                
                a.append(headA)
                headA=headA.next
                
            if headB:
                
                b.append(headB)
                headB=headB.next
            """
            """
            
        length=len(a)
        if length>len(b):
            length=len(b) 
        a=a[::-1]
        b=b[::-1]  
        a_previous=None
        b_previous=None
        for i in range(0,length):
            """
            """
            print("a:",a[i])
            print("b:",b[i])
            print("\n")
            
            if a[i]!=b[i]:
                return a_previous
            if i==length-1 and a[i]==b[i]:
            #若兩個串列在第一個就指向同一處，則前一個條件會失效
                return a[i]
            
            a_previous=a[i]
            b_previous=b[i]
            
        return None

a = ListNode(1)
a.next = ListNode(2)
a.next.next = ListNode(3)
a.next.next.next = ListNode(4)
a.next.next.next.next = ListNode(5)
a.next.next.next.next.next = ListNode(6)
a.next.next.next.next.next.next = ListNode(7)
a.next.next.next.next.next.next.next = ListNode(8)
a.next.next.next.next.next.next.next.next = ListNode(9)
a.next.next.next.next.next.next.next.next.next = ListNode(10)
a.next.next.next.next.next.next.next.next.next.next = ListNode(11)
a.next.next.next.next.next.next.next.next.next.next.next = ListNode(12)
a.next.next.next.next.next.next.next.next.next.next.next.next = ListNode(13)

b = a
b.next = a.next
b.next.next = a.next.next
b.next.next.next = a.next.next.next
b.next.next.next.next = a.next.next.next.next
b.next.next.next.next.next =a.next.next.next.next.next
b.next.next.next.next.next.next =a.next.next.next.next.next.next
b.next.next.next.next.next.next.next = a.next.next.next.next.next.next.next
b.next.next.next.next.next.next.next.next = a.next.next.next.next.next.next.next.next
b.next.next.next.next.next.next.next.next.next =a.next.next.next.next.next.next.next.next.next
b.next.next.next.next.next.next.next.next.next.next = a.next.next.next.next.next.next.next.next.next.next
b.next.next.next.next.next.next.next.next.next.next.next = a.next.next.next.next.next.next.next.next.next.next.next 
b.next.next.next.next.next.next.next.next.next.next.next.next = a.next.next.next.next.next.next.next.next.next.next.next.next


# Create an instance of Solution class
solution = Solution()

# Call the getIntersectionNode method to find the intersection point
intersection_node = solution.getIntersectionNode(a, b)

# Print the intersection node's value
if intersection_node:
    print("Intersection node value:", intersection_node.val)
else:
    print("No intersection")
