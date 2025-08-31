@PROBLEM:->
Given a string s in Roman number format, your task is to convert it to an integer. Various symbols and their values are given below.
Note: I = 1, V = 5, X = 10, L = 50, C = 100, D = 500, M = 1000

Examples:

Input: s = "IX"
Output: 9
Explanation: IX is a Roman symbol which represents 10 – 1 = 9.

Input: s = "XL"
Output: 40
Explanation: XL is a Roman symbol which represents 50 – 10 = 40.

Input: s = "MCMIV"
Output: 1904
Explanation: M is 1000, CM is 1000 – 100 = 900, and IV is 4. So we have total as 1000 + 900 + 4 = 1904.

Constraints:
1 ≤ roman number ≤ 3999
s[i] belongs to [I, V, X, L, C, D, M]

                      /********************************************************************/

SOLUTION:->

class Solution {
    public int romanToDecimal(String s) {
        int total = 0;
        int n = s.length();

        for (int i = 0; i < n; i++) {
            int cur = valueOf(s.charAt(i));
            int next = (i + 1 < n) ? valueOf(s.charAt(i + 1)) : 0;

            // If current value < next value → subtract
            if (cur < next) {
                total -= cur;
            } else {
                total += cur;
            }
        }
        return total;
    }

    private int valueOf(char c) {
        switch (c) {
            case 'I': return 1;
            case 'V': return 5;
            case 'X': return 10;
            case 'L': return 50;
            case 'C': return 100;
            case 'D': return 500;
            case 'M': return 1000;
            default: return 0;
        }
    }
}


