Smallest window containing 0, 1 and 2
Difficulty: EasyAccuracy: 49.73%Submissions: 67K+Points: 2
Given a string s consisting only of the characters '0', '1' and '2', determine the length of the smallest substring that contains all three characters at least once.

If no such substring exists, return -1.

Examples :

Input: s = "10212"
Output: 3
Explanation: The substring "102" is the shortest substring that contains all three characters '0', '1', and '2', so the answer is 3.
Input: s = "12121"
Output: -1
Explanation: The character '0' is not present in the string, so no substring can contain all three characters '0', '1', and '2'. Hence, the answer is -1.
Constraints:
1 ≤ s.size() ≤ 105

Expected Complexities
Time Complexity: O(n)
Auxiliary Space: O(1)
Company Tags
Paytm
Topic Tags
sliding-windowtwo-pointer-algorithmStringsData StructuresAlgorithms
Related Interview Experiences
Paytm Interview Experience 1 Year Experienced
Related Articles
Smallest Window Containing 0 1 And 2 

*/   ################################################################# */


class Solution:
    def smallestSubstring(self, s: str) -> int:
        n = len(s)
        
        count = [0, 0, 0]  # for '0', '1', '2'
        left = 0
        unique = 0
        min_len = float('inf')
        
        for right in range(n):
            idx = int(s[right])
            
            if count[idx] == 0:
                unique += 1
            count[idx] += 1
            
            # when all 3 chars present
            while unique == 3:
                min_len = min(min_len, right - left + 1)
                
                left_idx = int(s[left])
                count[left_idx] -= 1
                if count[left_idx] == 0:
                    unique -= 1
                left += 1
        
        return min_len if min_len != float('inf') else -1
