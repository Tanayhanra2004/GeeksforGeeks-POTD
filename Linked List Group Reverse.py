@Problem:->
You are given the head of a Singly linked list. You have to reverse every k node in the linked list and return the head of the modified list.
Note: If the number of nodes is not a multiple of k then the left-out nodes at the end, should be considered as a group and must be reversed.

Examples:

Input: k = 2,
   
Output: 2 -> 1 -> 4 -> 3 -> 6 -> 5
Explanation: Linked List is reversed in a group of size k = 2.
   
Input: k = 4,
   
Output: 4 -> 3 -> 2 -> 1 -> 6 -> 5
Explanation: Linked List is reversed in a group of size k = 4.
   
Constraints:
1 ≤ size of linked list ≤ 105
0 ≤ node->data ≤ 106
1 ≤ k ≤ size of linked list 

**********************************************

@Solution:->
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def reverseKGroup(self, head, k):
        if head is None or k <= 1:
            return head

        dummy = Node(0)
        dummy.next = head
        prev_group_end = dummy
        curr = head

        while curr:
            group_start = curr

            # Count up to k nodes (or fewer if at the end)
            count = 0
            while curr and count < k:
                curr = curr.next
                count += 1

            # Reverse exactly 'count' nodes
            prev = curr
            node = group_start
            for _ in range(count):
                nxt = node.next
                node.next = prev
                prev = node
                node = nxt

            prev_group_end.next = prev
            prev_group_end = group_start

        return dummy.next
