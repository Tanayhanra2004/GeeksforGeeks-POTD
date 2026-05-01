Kth Largest in a Stream
Difficulty: MediumAccuracy: 31.59%Submissions: 99K+Points: 4Average Time: 20m
Given an input stream arr[] of n integers. Find the Kth largest element (not Kth largest unique element) after insertion of each element in the stream and if the Kth largest element doesn't exist, the answer will be -1 for that insertion. 

Return a list of size n, where each element represents the Kth largest value after the corresponding insertion.

Examples :

Input: arr[] = [1, 2, 3, 4, 5, 6], k = 4
Output: [-1, -1, -1, 1, 2, 3]
Explanation: 
After 1, the steam is [1]. The 4th largest does not exist. Output is -1.
After 2, the stream is [1, 2]. The 4th largest does not exist. Output is -1.
After 3, the stream is [1, 2, 3]. The 4th largest does not exist. Output is -1.
After 4, the stream is [1, 2, 3, 4]. The 4th largest is 1.
After 5, the stream is [1, 2, 3, 4, 5]. The 4th largest is 2.
After 6, the stream is [1, 2, 3, 4, 5, 6]. The 4th largest is 3.
Input: arr[] = [3, 2, 1, 3, 3], k = 2
Output: [-1, 2, 2, 3, 3]
Explanation: 
After 3, the steam is [3]. Tthe 2nd largest does not exist. Output is -1.
After 2, the stream is [3, 2]. The 2nd largest is 2.
After 1, the stream is [3, 2, 1]. The 2nd largest is 2.
After 3, the stream is [3, 2, 1, 3]. The 2nd largest is 3.
After 3, the stream is [3, 2, 1, 3, 3]. The 2nd largest is 3.
Constraints:
1 ≤ k ≤ n ≤ 105
1 ≤ arr[i] ≤ 105



/*****************************************/


import heapq

class Solution:
    def kthLargest(self, arr, k):
        heap = []
        ans = []

        for num in arr:
            heapq.heappush(heap, num)

            # maintain only k largest elements
            if len(heap) > k:
                heapq.heappop(heap)

            if len(heap) < k:
                ans.append(-1)
            else:
                ans.append(heap[0])

        return ans

