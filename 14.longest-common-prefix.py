#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#
#
# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# @lc code=start
from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        idx = 0
        while True:
            if idx >= len(strs[0]):
                break
            current_char = strs[0][idx]
            valid_prefix = True
            for i in range(len(strs) - 1):
                if idx >= len(strs[i+1]) or strs[i+1][idx] != current_char:
                    valid_prefix = False
                    break
            if not valid_prefix:
                break
            res += current_char
            idx += 1
        return res

if __name__ == "__main__":
    s = Solution()
    print(s.longestCommonPrefix(["flower","flow","flight"]))
        
# @lc code=end

