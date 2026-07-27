from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:  
        pos = 0

        for i in range(len(nums)):
            if nums[pos] != nums[i]:
                pos = pos + 1
                nums[pos] = nums[i]

        return pos + 1