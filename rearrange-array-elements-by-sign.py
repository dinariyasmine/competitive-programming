class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = [num for num in nums if num > 0]
        neg = [num for num in nums if num < 0]
        if len(pos) == 0:
            pos.append(neg.pop())
        result = []
        for i in range(len(nums)//2):
            result.append(pos[i])
            result.append(neg[i])
        
        return result
            
