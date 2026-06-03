Subarray Frequency Count Queries
Difficulty: MediumAccuracy: 59.5%Submissions: 11K+Points: 4Average Time: 25m
Given an array arr[] of n integers and a 2D array queries[][] representing q queries, where each queries[i] consists of three integers: l, r, and x. For each query determine how many times the element x appears in the arr[] from index l to r (both inclusive).

Return a list of integers where the i-th value represents the answer to the i-th query.

Examples: 

Input: arr[] = [1, 2, 1, 3, 1, 2, 3], queries[][] = [[0, 4, 1], [2, 5, 2], [1, 6, 3], [0, 6, 5]]
Output: [3, 1, 2, 0]
Explanation:
query [0, 4, 1] -> Subarray = [1, 2, 1, 3, 1], 1 appears 3 times
query [2, 5, 2] -> Subarray = [1, 3, 1, 2], 2 appears 1 time
query [1, 6, 3] -> Subarray = [2, 1, 3, 1, 2, 3] 3 appears 2 times
query [0, 6, 5] -> Subarray = [1, 2, 1, 3, 1, 2, 3],  5 appears 0 times
Input: arr[] = [11, 21, 51, 101, 11, 51], queries[][] = [[0, 4, 11], [2, 5, 51]]
Output: [2, 2]
Explanation:
query [0, 4, 11] -> Subarray = [11, 21, 51, 101, 11], 11 appears 2 times
query [2, 5, 51] -> Subarray = [51, 101, 11, 51], 51 appears 2 times
Constraints:
1 ≤ arr.size(), queries.size() ≤ 105
1 ≤ arr[i], queries[i][2] ≤ 105
0 ≤ queries[i][0] ≤ queries[i][1] < arr.size()



/*******************************************************/

from bisect import bisect_left, bisect_right
from collections import defaultdict

class Solution:
    def freqInRange(self, arr, queries):
        mp = defaultdict(list)

        for i, val in enumerate(arr):
            mp[val].append(i)

        ans = []

        for l, r, x in queries:
            indexes = mp[x]

            left = bisect_left(indexes, l)
            right = bisect_right(indexes, r)

            ans.append(right - left)

        return ans
Expected Complexities
Time Complexity: O(n*log n + q*log k)
Auxiliary Space: O(n)
