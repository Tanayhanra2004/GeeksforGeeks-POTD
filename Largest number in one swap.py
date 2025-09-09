@PROBLEM->

Given a string s, return the lexicographically largest string that can be obtained by swapping at most one pair of characters in s.

Examples:

Input: s = "768"
Output: "867"
Explanation: Swapping the 1st and 3rd characters(7 and 8 respectively), gives the lexicographically largest string.
Input: s = "333"
Output: "333"
Explanation: Performing any swaps gives the same result i.e "333".
Constraints:
1 ≤ |s| ≤ 105
'0' ≤ s[i] ≤ '9'

*****************************
@SOLUTION:->
class Solution:
    def largestSwap(self, s):
        # Convert to list for swapping
        s_list = list(s)
        n = len(s_list)
        
        # Store the last occurrence of each digit
        last = {int(ch): i for i, ch in enumerate(s_list)}
        
        for i in range(n):
            # Check for larger digit from 9 down to current+1
            for d in range(9, int(s_list[i]), -1):
                if d in last and last[d] > i:
                    # Swap
                    s_list[i], s_list[last[d]] = s_list[last[d]], s_list[i]
                    return ''.join(s_list)  # Only one swap allowed
        
        return s  # Already largest, no swap needed
