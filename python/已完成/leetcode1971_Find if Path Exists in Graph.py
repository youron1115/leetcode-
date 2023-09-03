import time
class Solution(object):
    def validPath(self, n, edges, source, destination):
        #n = 3, edges = [[0,1],[1,2],[2,0],[3,4]], source = 0, destination = 4
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """
        if n==1:
            return True
        
        else:
            s_sets={source}
            d_sets={destination}
            #lens=len(edges)
            #len_new=0
            #valid=0
            start_time=time.time()
            while True:

                for e in edges:
                    if e[0] in s_sets or e[1] in s_sets:
                        s_sets.add(e[0])
                        s_sets.add(e[1])
                        #edges.remove(e)
                        
                    if e[0] in d_sets or e[1] in d_sets:
                        d_sets.add(e[0])
                        d_sets.add(e[1])
                        #edges.remove(e)
                    
                    if source in d_sets or destination in s_sets:
                        return True
                    
                if time.time() - start_time > 1:
                    print("迴圈可能進入無限迴圈狀態")
                    break
            return False