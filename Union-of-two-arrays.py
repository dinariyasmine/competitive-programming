#User function Template for python3

class Solution:    
    
    def doUnion(self,a,n,b,m):
        
        set_a = set(a)
        set_b = set(b)
   
        union_set = set_a.union(set_b)
  
        return len(union_set)



