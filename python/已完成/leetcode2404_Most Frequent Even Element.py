class Solution(object):
    def mostFrequentEven(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        nums.sort(reverse=True)
        #print("nums:",nums)        
        
        returns_key=-10
        returns_value=nums.count(returns_key)
        for n in nums:
            if n%2==1:
                continue
            else:
                if nums.count(n)>=returns_value:
                    returns_key=n
                    returns_value=nums.count(n)
        if returns_key<0:
            return -1
        return returns_key
        
s=Solution()
k=s.mostFrequentEven([29,47,21,41,13,37,25,7])
print("k:",k)
