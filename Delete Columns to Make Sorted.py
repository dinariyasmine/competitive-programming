class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        delet = 0
        for j in range(len(strs[0])):
            for i in range(1,len(strs)):
                if strs[i][j]<strs[i-1][j] :
                    delet += 1
                    break
        return delet
                
