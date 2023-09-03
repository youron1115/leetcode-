# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head==None:#空串列
            return head

        if head.next==None:#只有一個節點時
            return head
        """
        直接用k計算會導致記憶體占用過大
        先計算串列節點數
        將k/長度取餘數即為實際操作次數
        """
        test=start=head
        length=0

        while test!=None:
            length+=1
            test=test.next
        k%=length    

        for _ in range(0,k):
            pre=start
            
            while head.next!=None:
                pre=head
                head=head.next
            #head正在最後一個
            
            
            pre.next=head.next#次最後一個連向None   
            head.next=start#原最後一個的下一個連向第一個
            start=head#使原最後一個成為新的第一個

        return start

# 創建一個測試鏈表 [1, 2, 3, 4, 5]
node5 = ListNode(5)
node4 = ListNode(4, node5)
node3 = ListNode(3, node4)
node2 = ListNode(2, node3)
node1 = ListNode(1, node2)

# 創建 Solution 的實例
solution = Solution()

# 執行旋轉操作
k = 2
result = solution.rotateRight(node1, k)

# 輸出結果
output = []
while result != None:
    output.append(result.val)
    result = result.next

print(output)