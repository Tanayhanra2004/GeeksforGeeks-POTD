class Solution:
    def maxSumPairWithDifferenceLessThanK(self, arr, k):
        arr.sort()
        n = len(arr)

        dp = [0] * n
        dp[0] = 0

        for i in range(1, n):
            # Option 1: do not pair arr[i]
            dp[i] = dp[i - 1]

            # Option 2: pair arr[i-1] and arr[i]
            if arr[i] - arr[i - 1] < k:
                pair_sum = arr[i] + arr[i - 1]

                if i >= 2:
                    pair_sum += dp[i - 2]

                dp[i] = max(dp[i], pair_sum)

        return dp[n - 1]
