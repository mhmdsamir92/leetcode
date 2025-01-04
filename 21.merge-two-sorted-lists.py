#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]
#

# @lc code=start

from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    
    def printList(self, list: Optional[ListNode]) -> List:
        values = []
        current_node = list
        while (True):
            if current_node is not None:
                values.append(current_node.val)
            if current_node.next is None:
                break
            current_node = current_node.next
        return values


    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head_node = None
        tail_node = ListNode()
        i = -1
        j = 1
        current_node_i = list1
        current_node_j = list2
        while(True):
            if not current_node_i or not current_node_j:
                break
            smaller_idx = i
            smaller_node = current_node_i
            if current_node_i.val > current_node_j.val:
                smaller_idx = j
                smaller_node = current_node_j
            if head_node is None:
                tail_node.val = smaller_node.val
                head_node = tail_node
            else:
                new_tail = ListNode(smaller_node.val)
                tail_node.next = new_tail
                tail_node = new_tail
            if smaller_idx == i:
                current_node_i = current_node_i.next
            else:
                current_node_j = current_node_j.next
        new_tail = current_node_i if current_node_i else current_node_j
        if head_node is None:
            return new_tail
        tail_node.next = new_tail
        tail_node = new_tail
        return head_node        

if __name__ == "__main__":
    s = Solution()
    # list1 = ListNode(1, ListNode(2, ListNode(4)))
    list1 = ListNode
    list2 = ListNode(1, ListNode(3, ListNode(4)))
    print(s.printList(s.mergeTwoLists(list1, list2)))
# @lc code=end
