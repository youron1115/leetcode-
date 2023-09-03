class Solution(object):#more balance
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dicts={}
        returns=set()

        for n in nums:
            if n in dicts:
                dicts[n]+=1
                if dicts[n]>len(nums)/3:
                    returns.add(n)
            else:
                dicts[n]=1
                if dicts[n]>len(nums)/3:
                    returns.add(n)

        return list(returns)
    
"""
class Solution(object):#memory smaller
    def majorityElement(self, nums):
        
        #:type nums: List[int]
        #:rtype: List[int]
        
        dicts={}
        returns=set()

        for n in nums:
            if n in dicts:
                dicts[n]+=1
                if dicts[n]>len(nums)/3:
                    returns.add(n)
            else:
                dicts[n]=1
                if dicts[n]>len(nums)/3:
                    returns.add(n)

        return list(returns)
"""
    
    