from scipy.special import comb
#內含費氏(斐波那契)數列
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        total=0
        max_two=n//2
        
        for i in range(0,max_two+1):
            #每項都是2*i+剩下的
            #規則:每種都是(n-i)!/(n-2i)!
            total+=comb(n-i,n-2*i)
        return int(total)
        
            

a=Solution()
b=a.climbStairs(45)
print(b)

    