from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        answer = []

        for item in nums:
            if item != val:
                answer.append(item)

        for i in range(len(answer)):
            nums[i] = answer[i]

        return len(answer)