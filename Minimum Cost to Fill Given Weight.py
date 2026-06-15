Minimum Cost to Fill Given Weight
Difficulty: MediumAccuracy: 25.56%Submissions: 83K+Points: 4
Given a bag of size w kg and you are provided costs of packets different weights of oranges in array cost[], find the minimum total cost to buy exactly w kg oranges

The cost of 1 kg orange is present at index 0 and in general arr[i] has cost of (i+1) kg orange.
cost[i] = -1 means that 'i+1' kg packet of orange is unavailable.
If it is not possible to buy exactly w kg oranges then return -1. It may be assumed that there is an infinite supply of all available packet types.
Examples:

Input: cost[] = [20, 10, 4, 50, 100], w = 5
Output: 14
Explanation: The minimum cost is 14 by purchasing a 2kg packet for 10 and a 3kg packet for 4.
Input: cost[] = [-1, -1, 4, 3, -1], w = 5
Output: -1
Explanation: It is not possible to buy 5 kgs.
Constraints:
1 ≤ cost.size(), w ≤ 2*103
1 ≤ cost[i] ≤ 105
/*************************************************/

class Solution:
    def minimumCost(self, cost, w):
        n = len(cost)
        INF = 10**18

        dp = [INF] * (w + 1)
        dp[0] = 0

        for i in range(n):
            packet_weight = i + 1
            packet_cost = cost[i]

            if packet_cost == -1:
                continue

            for weight in range(packet_weight, w + 1):
                if dp[weight - packet_weight] != INF:
                    dp[weight] = min(dp[weight], dp[weight - packet_weight] + packet_cost)

        return -1 if dp[w] == INF else dp[w]
