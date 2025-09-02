@PROBLEM:->
Given the head of a singly linked list and an integer k. Swap the kth node (1-based index) from the beginning and the kth node from the end of the linked list. Return the head of the final formed list and if it's not possible to swap the nodes return the original list.

Examples:

Input: k = 1,
  
Output: 5 -> 2 -> 3 -> 4 -> 1
Explanation: Here k = 1, hence after swapping the 1st node from the beginning and end the new list will be 5 -> 2 -> 3 -> 4 -> 1.
  
Input: k = 2,
  
Output: 5 -> 9 -> 8 -> 5 -> 10 -> 3
Explanation: Here k = 2, hence after swapping the 2nd node from the beginning and end the new list will be 5 -> 9 -> 8 -> 5 -> 10 -> 3.
  
Constraints:
1 ≤ list size ≤ 104
1 ≤ node->data ≤ 106
1 ≤ k ≤ 104

*************************************************************

@Solution:->
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None

class Solution:
    def swapKth(self, head, k):
        # Step 1: Find length of the list
        n = 0
        temp = head
        while temp:
            n += 1
            temp = temp.next

        # Step 2: If k is invalid
        if k > n:
            return head

        # Step 3: If swapping the same node
        if 2 * k - 1 == n:
            return head

        # Step 4: Find kth node from start
        first = head
        for _ in range(k - 1):
            first = first.next

        # Step 5: Find kth node from end (n-k+1 from start)
        second = head
        for _ in range(n - k):
            second = second.next

        # Step 6: Swap data
        first.data, second.data = second.data, first.data

        return head

