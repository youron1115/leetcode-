class Solution(object):
    def lengthOfLongestSubstring(self, s):
        max_number=0
        max_sub=""
        for i in range(len(s)):
            j=i
            sub=""
            seen=set()
            while s[j] not in seen :
                sub+=s[j]
                seen.add(s[j])
                if j+1==len(s):
                    break
                j+=1
            if len(sub)>max_number:
                max_number=len(sub)
                max_sub=sub
        return  max_number