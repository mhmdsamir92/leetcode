#
# @lc app=leetcode id=162 lang=python3
#
# [162] Find Peak Element
#

from typing import List
import math

# @lc code=start
class Solution:
    nums: List[int]
    def getElementAt(self, idx: int):
        if idx < 0 or idx == len(self.nums):
            return -1 * math.inf
        return self.nums[idx]
    def findPeakElement(self, nums: List[int]) -> int:
        self.nums = nums
        start = 0
        end = len(nums) - 1
        mid = (end + start) // 2
        mid_value = self.getElementAt(mid)
        right_mid_adj = self.getElementAt(mid + 1)
        left_mid_adj = self.getElementAt(mid - 1)
        while mid_value < left_mid_adj or mid_value < right_mid_adj:
            if mid_value < left_mid_adj:
                end = mid - 1
            else:
                start = mid + 1
            if start == end:
                return start
            mid = (end + start) // 2
            mid_value = self.getElementAt(mid)
            right_mid_adj = self.getElementAt(mid + 1)
            left_mid_adj = self.getElementAt(mid - 1)
        return mid

if __name__ == "__main__":
    s = Solution()
    print(s.findPeakElement([1, 2]))
# @lc code=end

