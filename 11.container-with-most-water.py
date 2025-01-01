#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

from typing import List

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        maxArea = 0
        while i != j:
            current_width = j - i
            min_bar = i if height[i] < height[j] else j
            current_height = height[min_bar]
            current_area = current_width * current_height
            if current_area > maxArea:
                maxArea = current_area
            if min_bar == i:
                i += 1
            else:
                j -= 1
        return maxArea

if __name__ == "__main__":
    s = Solution()
    print(s.maxArea([1,1]))

# @lc code=end

