#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#
from typing import List
# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        pointer_i = 0
        pointer_j = 0
        current_num = nums[0]
        unique_count = 0
        while pointer_j < len(nums):
            if nums[pointer_j] <= current_num:
                pointer_j += 1
            else:
                pointer_i += 1
                current_num = nums[pointer_j]
                if nums[pointer_i] != nums[pointer_j]:
                    temp = nums[pointer_i]
                    nums[pointer_i] = nums[pointer_j]
                    nums[pointer_j] = temp
                unique_count += 1
        return unique_count + 1
                
# if __name__ == "__main__":
#     s = Solution()
#     nums = [1,2,3]
#     print(s.removeDuplicates(nums))
#     s.removeDuplicates(nums)
#     print(nums)
        
# @lc code=end

