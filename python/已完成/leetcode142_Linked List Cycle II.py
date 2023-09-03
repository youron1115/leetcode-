#解法一
"""
class Solution(object):
    def detectCycle(self, head):
        
        #type head: ListNode
        #rtype: ListNode
        
        print("一次測試\n")
        if head==None:
            print("首次測試\n")
            return None
        
        recorder=set()
        
        
        while head.next!=None:
            
            if head.next in recorder:
                print("in測試\n")
                
                
                return head.next
                
            else:
                print("鏈結測試\n")
                recorder.add(head)
                head=head.next
        print("最後測試\n")  
        return None
"""



# 創建測試用例


# 創建解決方案對象
solution = Solution()

# 測試 detectCycle 方法



head = ListNode(3)
head.next=ListNode(2)
head.next.next=ListNode(0)
head.next.next.next=ListNode(4)
head.next.next.next.next=head.next

result = solution.detectCycle(head)
print(type(result))

# 輸出結果
if result:
    print("Output: tail connects to node index", result.val)
else:
    print("Output: No cycle")