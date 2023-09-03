"""
class Solution(object):#memory smaller
    def majorityElement(self, nums):
        
        #:type nums: List[int]
        #:rtype: int
        
        
        
        
        major=nums[0]
        dicts={}
        
        for i in nums:
            if i in dicts:
                dicts[i]+=1
            else:
                dicts[i]=1
        
        for i in dicts:
            if dicts[i]>len(nums)/2:
                major=i
            
            
        return major
        
        """
class Solution(object):#faster
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dicts={}
        for i in nums:
            if i in dicts:
                dicts[i]+=1
                if dicts[i]>len(nums)/2:
                    return i
            else:
                dicts[i]=1

lists=[47,47,72,47,72,47,79,47,12,92,13,47,47,83,33,15,18,47,47,47,47,64,47,65,47,47,47,47,70,47,47,55,47,15,60,47,47,47,47,47,46,30,58,59,47,47,47,47,47,90,64,37,20,47,100,84,47,47,47,47,47,89,47,36,47,60,47,18,47,34,47,47,47,47,47,22,47,54,30,11,47,47,86,47,55,40,49,34,19,67,16,47,36,47,41,19,80,47,47,27]
s=Solution()
a=s.majorityElement(lists)
print(a)