Given a binary string s consisting of 0s and 1s. Find the maximum difference of the number of 0s and the number of 1s (number of 0s – number of 1s) in a substring of the string.

Note: In the case of all 1s, the answer will be -1.

Examples:

Input : s = "11000010001" 
Output : 6 
Explanatio: From index 2 to index 9, there are 7 0s and 1 1s, so number of 0s - number of 1s is 6. 
Input: s = "111111"
Output: -1
Explanation: s contains 1s only 
Constraints:
1 ≤ s.size() ≤ 105

Expected Complexities
Time Complexity: O(n)
Auxiliary Space: O(1)
Topic Tags
StringsDynamic ProgrammingKadaneData StructuresAlgorithms
Related Articles
Maximum Difference Zeros Ones Binary String

/*****************************************/

class Solution:
    def maxSubstring(self, s):
        max_sum = -1
        curr_sum = 0
        
        for ch in s:
            val = 1 if ch == '0' else -1
            
            curr_sum += val
            max_sum = max(max_sum, curr_sum)
            
            if curr_sum < 0:
                curr_sum = 0
        
        return max_sum
