@Problem:->

You are given the head of a doubly linked list. You have to reverse the doubly linked list and return its head.

Examples:

Input:
   
Output: 5 <-> 4 <-> 3
Explanation: After reversing the given doubly linked list the new list will be 5 <-> 4 <-> 3.
   
Input: 
   
Output: 196 <-> 59 <-> 122 <-> 75
Explanation: After reversing the given doubly linked list the new list will be 196 <-> 59 <-> 122 <-> 75.
   
Constraints:
1 ≤ number of nodes ≤ 106
0 ≤ node->data ≤ 104

***************************************

@SOlution:-.

class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None


class Solution:
    def reverse(self, head):
        if not head or not head.next:
            return head  # empty or single node

        curr = head
        prev = None

        while curr:
            # swap next and prev
            prev = curr.prev
            curr.prev = curr.next
            curr.next = prev
            # move to next node (which was prev originally)
            curr = curr.prev

        # prev will be at the old head, so new head is prev.prev
        return prev.prev
