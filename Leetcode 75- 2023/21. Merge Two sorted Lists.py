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


class Node:
    def __init__(self, val=0, nxt=None):
        self.val = val
        self.nxt = nxt


class SLinkedList:
    def __init__(self):
        self.headval = None

    # Function to add new Node at the end
    def addNode(self, newNode):
        NewNode = Node(newNode)
        if self.headval is None:
            self.headval = NewNode
            return
        tail = self.headval
        while tail.nxt:
            tail = tail.nxt
        tail.nxt = NewNode

    # Print the linked list
    def printList(self):
        tail = self.headval
        while tail:
            print(tail.val)
            tail = tail.nxt


list1 = SLinkedList()
list1.addNode(1)
list1.addNode(2)
list1.addNode(3)

list1.printList()

