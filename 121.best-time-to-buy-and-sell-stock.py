#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

from typing import List

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_solution = 0
        current_min_idx = 0
        for idx in range(len(prices)):
            n = prices[idx]
            if (n - prices[current_min_idx]) > max_solution:
                max_solution = n - prices[current_min_idx]
            if n < prices[current_min_idx]:
                current_min_idx = idx
        return max_solution


# if __name__ == "__main__":
#     s = Solution()
#     print(s.maxProfit([7,6,4,3,1]))
# @lc code=end

