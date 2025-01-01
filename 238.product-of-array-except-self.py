#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

from typing import List
from collections import deque

# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_product = deque([1])
        right_product = deque([1])
        for idx in range(len(nums) - 1):
            left_product.append(left_product[idx] * nums[idx])
        for idx in range(len(nums) - 1):
            right_product.appendleft(right_product[-1 * (idx + 1)] * nums[-1 * (idx + 1)])
        result = []
        for idx in range(len(right_product)):
            result.append(right_product[idx] * left_product[idx])
        return result

if __name__ == "__main__":
    s = Solution()
    print(s.productExceptSelf([-1,1,0,-3,3]))
# @lc code=end

