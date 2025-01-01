#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

from collections import deque

# @lc code=start
class Solution:
    def corresponding(self, c: str):
        if c == '(':
            return ')'
        if c == '[':
            return ']'
        if c == '{':
            return '}'

    def isValid(self, s: str) -> bool:
        par_stack = deque()
        for character in s:
            if character in ['(', '[', '{']:
                par_stack.append(character)
            else:
                if len(par_stack) == 0:
                    return False
                stack_top = par_stack.pop()
                if character != self.corresponding(stack_top):
                    return False
        return False if len(par_stack) else True

# if __name__ == "__main__":
#     s = Solution()
#     print(s.isValid("(]"))
# @lc code=end