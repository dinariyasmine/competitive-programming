
class Solution:
    #Function to check if two arrays are equal or not.
    def check(self,A,B,N):
        
        setA = set(A)
        setB = set(B)
        
        return setA == setB