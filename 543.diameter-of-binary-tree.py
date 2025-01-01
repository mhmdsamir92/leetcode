#
# @lc app=leetcode id=543 lang=python3
#
# [543] Diameter of Binary Tree
#
from typing import Optional
# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        left_height = 1 + self.diameterOfBinaryTree(root.left)
        right_height = 1 + self.diameterOfBinaryTree(root.right)
        return left_height + right_height
# @lc code=end

