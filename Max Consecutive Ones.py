class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max = 0
        list_of_max = []
        for i in nums:
            if i == 1:
                max += 1
            else:
                list_of_max.append(max)
                max = 0
            list_of_max.append(max)
        sorted_list_of_max= sorted(list_of_max, reverse = True)

        return sorted_list_of_max[0]
        