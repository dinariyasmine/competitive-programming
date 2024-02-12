from ast import List

class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        
        start = (num - 3) // 3
        
        
        if start * 3 + 3 == num:
            return [start, start + 1, start + 2]
        else:
            return []
