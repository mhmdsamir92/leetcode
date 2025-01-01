#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

from typing import List
import math
# -2 1 -3 4 -1 2 1 -5 4
# result  = 5
# counter = 5
# num     = 1
# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = -1 * math.inf
        counter = 0
        for num in nums:
            if num > counter:
                counter = max(num, counter + num)
            else:
                counter += num
            if counter > result:
                result = counter
        if counter > result:
                result = counter
        return result

# if __name__ == "__main__":
#     s = Solution()
#     print(s.maxSubArray([1,2]))


        
# @lc code=end

