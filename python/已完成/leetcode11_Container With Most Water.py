class Solution(object):
    def maxArea(self, height):
        print(len(height))
        max_water=0
        while len(height)>2:
            
            #print("width:",(len(height)-1),"high:",min(height[0],height[-1]),"part_max:",(len(height)-1)*min(height[0],height[-1]))
            max_water=max((len(height)-1)*min(height[0],height[-1]),max_water)

            if height[0]>height[-1]:
                del height[-1]
            else:
                del height[0]
        
        max_water=max((len(height)-1)*min(height[0],height[-1]),max_water)
        return max_water