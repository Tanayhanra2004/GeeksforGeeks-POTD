@PROBLEM :->

A celebrity is a person who is known to all but does not know anyone at a party. A party is being organized by some people. A square matrix mat[][] of size n*n is used to represent people at the party such that if an element of row i and column j is set to 1 it means ith person knows jth person. You need to return the index of the celebrity in the party, if the celebrity does not exist, return -1.

Note: Follow 0-based indexing.

Examples:

Input: mat[][] = [[1, 1, 0],
                [0, 1, 0],
                [0, 1, 1]]
Output: 1
Explanation: 0th and 2nd person both know 1st person and 1st person does not know anyone. Therefore, 1 is the celebrity person.
Input: mat[][] = [[1, 1], 
                [1, 1]]
Output: -1
Explanation: Since both the people at the party know each other. Hence none of them is a celebrity person.
Input: mat[][] = [[1]]
Output: 0
Constraints:
1 ≤ mat.size() ≤ 1000
0 ≤ mat[i][j] ≤ 1
mat[i][i] = 1

**************************************************************************************************************************

@ SOLUTION:->

class Solution {
    // Function to find the celebrity
    public int celebrity(int[][] mat) {
        int n = mat.length;
        int left = 0, right = n - 1;

        // Step 1: Find potential celebrity
        while (left < right) {
            if (mat[left][right] == 1) {
                // left knows right → left can't be celebrity
                left++;
            } else {
                // left doesn't know right → right can't be celebrity
                right--;
            }
        }

        int candidate = left;

        // Step 2: Verify candidate
        for (int i = 0; i < n; i++) {
            if (i != candidate) {
                // celebrity should not know anyone
                if (mat[candidate][i] == 1) return -1;
                // everyone should know celebrity
                if (mat[i][candidate] == 0) return -1;
            }
        }

        return candidate;
    }

    // Example usage
    public static void main(String[] args) {
        Solution sol = new Solution();

        int[][] mat1 = {{1, 1, 0},
                        {0, 1, 0},
                        {0, 1, 1}};
        System.out.println(sol.celebrity(mat1));  // Output: 1

        int[][] mat2 = {{1, 1}, {1, 1}};
        System.out.println(sol.celebrity(mat2));  // Output: -1

        int[][] mat3 = {{1}};
        System.out.println(sol.celebrity(mat3));  // Output: 0
    }
}
