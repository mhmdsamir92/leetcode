#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        symbols_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
            'IV': 4,
            'IX': 9,
            'XL': 40,
            'XC': 90,
            'CD': 400,
            'CM': 900
        }
        result = 0;
        current_idx = 0
        while current_idx < len(s):
            symbol_to_lookup = s[current_idx]
            current_num = symbols_map[symbol_to_lookup]
            if current_idx + 1 < len(s) and (symbol_to_lookup + s[current_idx + 1]) in symbols_map:
                current_num = symbols_map[symbol_to_lookup + s[current_idx + 1]]
                current_idx += 1
            current_idx += 1
            result += current_num
        return result

if __name__ == "__main__":
    s = Solution()
    print(s.romanToInt("MCMXCIV"))
        
# @lc code=end