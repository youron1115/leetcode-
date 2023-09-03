#解法1:超過時間
"""
class Solution(object):
    def threeSum(self, nums):
        
        #:type nums: List[int]
        #:rtype: List[List[int]]
        
        
        
        if len(nums)==3 and sum(nums)==0:  
            return [nums]
        else:
            nums.sort()
            print("nums:")
            print(nums)
            lists=list()
            if nums.count(0)!=0 and nums.count(0)%3==0:
                        
                lists.append([0,0,0])
            
            for i in range(0,len(nums)):
                #print ("i:",i)
                for j in range(0,len(nums)):
                 #   print ("i:",i,"j:",j)
                    if j!=i:
                        for k in range(len(nums)):
                  #          print ("i:",i,"j:",j,"k",k)
                            if k!=j and k!=i:
                                if nums[k]+nums[i]+nums[j]==0:
                                        
                                    lists.append([nums[i],nums[j],nums[k]])
            print("list:")
            print(lists)
            sets=set()
            for i in range(len(lists)):
                lists[i].sort()
                sets.add(tuple(lists[i]))
            
            print("sets:")
            print(sets)
            lists2=list(sets)
            print("lists2")
            print(lists2)
            print("本測試結束！")
            return lists2
            
"""

#解法2:超過時間
"""
class Solution(object):
    def threeSum(self, nums):
        
        #:type nums: List[int]
        #:rtype: List[List[int]]
        
        
        
        if len(nums)==3 and sum(nums)==0:  
            return [nums]

        else:
            lists=[]
            nums.sort()
            neg=[]
            pos=[]
            if nums.count(0)>2:
                lists.append([0,0,0])

            for i in nums:
                if i<0:
                    neg.append(i)
                elif i>0:
                    pos.append(i)
                else:
                    continue
            
            #print("neg:",neg)
            #print("pos:",pos)
            
            for i in range(len(neg)):
                target=0-neg[i]
                #print("target:",target)
                if target in pos and (0 in nums):#相反數加上0
                    
                    lists.append([neg[i],0,target])
                    #print("target is in pos!")
                
                for j in range(len(neg)):#兩個負數+一個正數
                    if j!=i:
                        for k in range(len(pos)):
                            #print("i:",i,"j:",j,"k:",k)
                            if pos[k]==target-neg[j]:
                                #print("list:",neg[i],neg[j],pos[k])
                                
                                lists.append([neg[i],neg[j],pos[k]])
                #print("接下來是兩正一負")                    
                for j in range(len(pos)):#兩個正數+一個負數
                    
                    for k in range(len(pos)):
                        #print("i:",i,"j:",j,"k:",k)
                        if k!=i and k!=j and pos[k]==target-pos[j]:
                            #print("list:",neg[i],pos[j],pos[k])
                                
                            lists.append([neg[i],pos[j],pos[k]])
            
            sets=set()
            for i in lists:
                sets.add(tuple(sorted(i)))

            lists2=list(sets)
            
            #for i in range(len(lists2)):
             #   lists2[i]=list(lists2[i])
                          
            return lists2
        """

#解法3
class Solution(object):
        
    def threeSum(self,nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.nums=nums
        
        if len(self.nums)==3: 
            if sum(self.nums)==0:  
                return [self.nums]

        else:
            sets=set()
            nums.sort()
            neg=[]
            
            pos=[]
            
            zero=[]
            
            if self.nums.count(0)>2:
                sets.add((0,0,0))

            for i in self.nums:
                if i<0:
                    neg.append(i)
                elif i>0:
                    pos.append(i)
                else:
                    zero.append(i)
            N=set(neg)
            P=set(pos)
            """
            print("neg:",neg)
            print("pos:",pos)
            """
            if zero:
                for i in N:#相反數加上0
                    #print("現在i=",i)
                    target=i*-1
                    #print("target:",target)
                    if target in P:
                        """
						print("i:",i)
                        print("0:",0)
                        print("target:",target)
                        """
                        sets.add((0,i,target))
                        #print("target is in pos!")
                    
            for i in range(len(neg)): #兩個負數+一個正數
                
                for j in range(i+1,len(neg)):
                    
                    #print("i:",i,"j:",j,"k:",0-neg[i]-neg[j])
                    if 0-neg[i]-neg[j] in P:
                        #print("list:",neg[i],neg[j],0-neg[i]-neg[j])
                                
                        sets.add(tuple((neg[i],neg[j],0-neg[i]-neg[j])))
            #print("接下來是兩正一負")     
            for i in range(len(pos)):#兩個正數+一個負數       
                for j in range(i+1,len(pos)):
                    
                    
                    #print("i:",i,"j:",j,"k:",0-pos[i]-pos[j])
                    if 0-pos[i]-pos[j] in N:
                        #print("list:",i,pos[j],0-pos[i]-pos[j])
                                
                        sets.add(tuple((pos[i],pos[j],0-pos[i]-pos[j])))
            
            return sets
        
        