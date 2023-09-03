class Solution(object):
    def findCenter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        #要嘛是[0]元素相等要嘛[1]相等
        if edges[0][0]==edges[1][0] or edges[0][0]==edges[1][1]:
            #若[0]元素相等，必會跟[1][0]or[1][1]相等
            return edges[0][0]
        return edges[0][1]