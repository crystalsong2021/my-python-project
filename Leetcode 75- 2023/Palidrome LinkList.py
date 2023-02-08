"""
234. Palindrome Linked List
Given the head of a singly linked list, return true if it is a
palindrome or false otherwise.

Example 1:

Input: head = [1,2,2,1]
Output: true
Example 2:

Input: head = [1,2]
Output: false

Constraints:

The number of nodes in the list is in the range [1, 105].
0 <= Node.val <= 9


Follow up: Could you do it in O(n) time and O(1) space?
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# use fast and slow pointer
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        tail = head
        newList = []
        while tail:
            newList.append(tail.val)
            tail = tail.next
        print(newList)

        rightPointer = len(newList) - 1
        # compare with two pointer
        for i in range(len(newList) // 2):
            if newList[i] != newList[rightPointer]:
                return False
            rightPointer -= 1

        return True