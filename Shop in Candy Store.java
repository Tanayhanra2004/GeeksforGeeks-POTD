In a candy store, there are different types of candies available and prices[i] represent the price of  ith types of candies. You are now provided with an attractive offer.
For every candy you buy from the store, you can get up to k other different candies for free. Find the minimum and maximum amount of money needed to buy all the candies.
Note: In both cases, you must take the maximum number of free candies possible during each purchase.

Examples :

Input: prices[] = [3, 2, 1, 4], k = 2
Output: [3, 7]
Explanation: As according to the offer if you buy one candy you can take at most k more for free. So in the first case, you buy the candy worth 1 and takes candies worth 3 and 4 for free, also you need to buy candy worth 2. So min cost: 1+2 = 3. In the second case, you can buy the candy worth 4 and takes candies worth 1 and 2 for free, also you need to buy candy worth 3. So max cost: 3+4 = 7.
Input: prices[] = [3, 2, 1, 4, 5], k = 4
Output: [1, 5]
Explanation: For minimimum cost buy the candy with the cost 1 and get all the other candies for free. For maximum cost buy the candy with the cost 5 and get all other candies for free.
Constraints:
1 ≤ prices.size() ≤ 105
0 ≤ k ≤ prices.size()
1 ≤ prices[i] ≤ 104

/*******************************************************/

@SOLUTION:->

import java.util.*;

class Solution {
    public ArrayList<Integer> minMaxCandy(int[] prices, int k) {
        ArrayList<Integer> ans = new ArrayList<>();
        Arrays.sort(prices); // Sort the prices

        int n = prices.length;

        // -------- Minimum cost --------
        int minCost = 0;
        int buy = 0, free = n - 1;
        while (buy <= free) {
            minCost += prices[buy];
            buy++;
            free -= k; // get k candies free
        }

        // -------- Maximum cost --------
        int maxCost = 0;
        buy = n - 1;
        free = 0;
        while (free <= buy) {
            maxCost += prices[buy];
            buy--;
            free += k; // get k cheapest candies free
        }

        ans.add(minCost);
        ans.add(maxCost);
        return ans;
    }

    // For testing
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String[] arr = sc.nextLine().trim().split(" ");
        int n = arr.length;
        int[] prices = new int[n];
        for (int i = 0; i < n; i++) {
            prices[i] = Integer.parseInt(arr[i]);
        }
        int k = sc.nextInt();

        Solution ob = new Solution();
        ArrayList<Integer> res = ob.minMaxCandy(prices, k);
        System.out.println(res.get(0) + " " + res.get(1));
    }
}


