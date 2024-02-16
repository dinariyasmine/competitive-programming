class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        n = len(nums)
        right = []
        left = []
        pivots = []
        for num in nums:
            if num < pivot :
                right.append(num)
            elif num > pivot:
                left.append(num)
            else:
                pivots.append(num)
        output = []
        for rig in right :
            output.append(rig)
        for piv in pivots :
            output.append(piv)
        for lef in left :
            output.append(lef)
        return output
