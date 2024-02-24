class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        n = len(nums)
        count_0 = nums.count(0)
        count_1 = nums.count(1)
        highest_index = []
        highest_score = float('-inf') 
        count_left_0 = 0
        for i in range(0, n+1):
            if i != 0:
                if nums[i-1] == 0:
                    count_left_0 += 1
            score = count_left_0 + (count_1 - (i - count_left_0))
            if score > highest_score:
                highest_index = [i]
                highest_score = score
            elif score == highest_score:
                highest_index.append(i)
        
        return highest_index
