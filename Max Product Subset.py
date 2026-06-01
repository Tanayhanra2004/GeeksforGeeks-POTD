Given an array arr[], find and return the maximum product possible with the subset of elements present in the array.

Note:

The maximum product can be of a single element also.
Since the product can be large, return it modulo 109 + 7.
Examples:

Input: arr[] = [-1, 0, -2, 4, 3]
Output: 24
Explanation: Maximum product will be ( -1 * -2 * 4 * 3 ) = 24
Input: arr[] = [-1, 0]
Output: 0
Explanation: Maximum product will be ( -1 * 0) = 0
Input: arr[] = [5]
Output: 5
Explanation: Maximum product will be 5.
Constraints:
1 ≤ arr.size() ≤ 2 * 104
-10 ≤ arr[i] ≤ 10

/**********************************************************/

class Solution:
    def findMaxProduct(self, arr):
        MOD = 10**9 + 7
        
        if len(arr) == 1:
            return arr[0]
        
        zero = 0
        neg = 0
        max_neg = -11
        product = 1
        
        for x in arr:
            if x == 0:
                zero += 1
                continue
            
            if x < 0:
                neg += 1
                max_neg = max(max_neg, x)
            
            product = (product * x) % MOD
        
        if zero == len(arr):
            return 0
        
        if neg == 1 and zero + neg == len(arr):
            return 0
        
        if neg % 2 == 1:
            product = (product * pow(max_neg, MOD - 2, MOD)) % MOD
        
        return product
