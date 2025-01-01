#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input Array Is Sorted
#

# @lc code=start

from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1
        while i != j:
            current_sum = numbers[i] + numbers[j]
            if current_sum == target:
                return [i + 1, j + 1]
            if current_sum > target:
                j -= 1
            else:
                i += 1
        return []

if __name__ == "__main__":
    s = Solution()
    print(s.twoSum([2,7,11,15], 9))
            

# @lc code=end

