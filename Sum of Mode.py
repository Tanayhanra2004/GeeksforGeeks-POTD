@PROBLEM:->

Given an array arr[] of positive integers and an integer k. You have to find the sum of the modes of all the subarrays of size k.
Note: The mode of a subarray is the element that occurs with the highest frequency. If multiple elements have the same highest frequency, the smallest such element is considered the mode.

Examples:

Input: arr[] = [1, 2, 3, 2, 5, 2, 4, 4], k = 3
Output: 13
Explanation: The mode of each k size subarray is [1, 2, 2, 2, 2, 4] and sum of all modes is 13.

Input: arr[] = [1, 2, 1, 3, 5], k = 2
Output: 6
Explanation: The mode of each k size subarray is [1, 1, 1, 3] and sum of all modes is 6.

Constraints:
1 ≤ k ≤ arr.size() ≤105
1 ≤ arr[i] ≤ 105

/************************************/

from collections import defaultdict
import heapq

class Solution:
    def sumOfModes(self, arr, k):
        n = len(arr)
        
        # freq map of each element
        freq = defaultdict(int)
        
        # bucket of elements by frequency
        bucket = defaultdict(list)   # freq -> min-heap of elements
        in_bucket = defaultdict(set) # to handle lazy deletion
        
        maxFreq = 0
        result = 0
        
        # helper to clean heap top
        def get_min_from_bucket(f):
            while bucket[f] and bucket[f][0] not in in_bucket[f]:
                heapq.heappop(bucket[f])
            return bucket[f][0] if bucket[f] else None
        
        # build first window
        for i in range(k):
            val = arr[i]
            oldf = freq[val]
            newf = oldf + 1
            freq[val] = newf
            if oldf > 0:
                in_bucket[oldf].discard(val)
            heapq.heappush(bucket[newf], val)
            in_bucket[newf].add(val)
            maxFreq = max(maxFreq, newf)
        
        mode = get_min_from_bucket(maxFreq)
        result += mode
        
        # slide window
        for i in range(k, n):
            out_val = arr[i-k]
            in_val = arr[i]
            
            # remove outgoing
            oldf = freq[out_val]
            freq[out_val] -= 1
            in_bucket[oldf].discard(out_val)
            if freq[out_val] > 0:
                newf = oldf - 1
                heapq.heappush(bucket[newf], out_val)
                in_bucket[newf].add(out_val)
            
            # add incoming
            oldf = freq[in_val]
            newf = oldf + 1
            freq[in_val] = newf
            if oldf > 0:
                in_bucket[oldf].discard(in_val)
            heapq.heappush(bucket[newf], in_val)
            in_bucket[newf].add(in_val)
            maxFreq = max(maxFreq, newf)
            
            # adjust maxFreq if needed
            while maxFreq > 0 and not in_bucket[maxFreq]:
                maxFreq -= 1
            
            mode = get_min_from_bucket(maxFreq)
            result += mode
        
        return result
