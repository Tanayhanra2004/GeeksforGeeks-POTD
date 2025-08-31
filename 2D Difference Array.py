@PROBLEM:->

You are given a 2D integer matrix mat[][] of size n × m and a list of q operations opr[][]. Each operation is represented as an array [v, r1, c1, r2, c2], where:

v is the value to be added
(r1, c1) is the top-left cell of a submatrix
(r2, c2) is the bottom-right cell of the submatrix (inclusive)
For each of the q operations, add v to every element in the submatrix from (r1, c1) to (r2, c2). Return the final matrix after applying all operations.

Examples:

Input: mat[][] = [[1, 2, 3],  opr[][] = [[2, 0, 0, 1, 1], [-1, 1, 0, 2, 2]]
                [1, 1, 0],
                [4,-2, 2]]
Output: [[3, 4, 3],
        [2, 2, -1],
        [3, -3, 1]] 
Explanation: 
 
Constraint:
1 ≤ n×m, q ≤ 105
0 ≤ r1 ≤ r2 ≤ n - 1
0 ≤ c1 ≤ c2 ≤ m - 1
-104 ≤ mat[i][j], v ≤ 104

**************************************************
SOLUTION:->

class Solution:
    def applyDiff2D(self, mat, opr):
        n, m = len(mat), len(mat[0])
        diff = [[0]*(m+1) for _ in range(n+1)]
        
        # Step 1: Apply difference updates
        for v, r1, c1, r2, c2 in opr:
            diff[r1][c1] += v
            if c2 + 1 < m:
                diff[r1][c2+1] -= v
            if r2 + 1 < n:
                diff[r2+1][c1] -= v
            if r2 + 1 < n and c2 + 1 < m:
                diff[r2+1][c2+1] += v
        
        # Step 2: Prefix sum row-wise
        for i in range(n):
            for j in range(1, m):
                diff[i][j] += diff[i][j-1]
        
        # Step 3: Prefix sum col-wise
        for j in range(m):
            for i in range(1, n):
                diff[i][j] += diff[i-1][j]
        
        # Step 4: Apply diff to original matrix
        for i in range(n):
            for j in range(m):
                mat[i][j] += diff[i][j]
        
        return mat
