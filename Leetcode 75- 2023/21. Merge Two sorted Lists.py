"""
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists in a one sorted list. The list should be made
by splicing together the nodes of the first two lists.
Return the head of the merged linked list.

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Input: list1 = [], list2 = []
Output: []

Input: list1 = [], list2 = [0]
Output: [0]

1. need to add the numbers to the  list1 and list2
"""


class ListNode:
    def __init__(self, val=0, nxt=None):
        self.nxt = nxt
        self.val = val


list1 = ListNode(1)
list1.nxt = ListNode(2)
list1.nxt.nxt = ListNode(4)
print(list1.val, list1.nxt.val, list1)
