/*
Given an integer n, calculate the sum of series 13 + 23 + 33 + 43 + … till n-th term.

Examples:

Input: n = 5
Output: 225
Explanation: 13 + 23 + 33 + 43 + 53 = 225
Input: n = 7
Output: 784
Explanation: 13 + 23 + 33 + 43 + 53 + 63 + 73 = 784
Expected Time Complexity: O(1)
Expected Auxillary Space: O(1)

Constraints:
1 <= n <= 5 * 104 
*/



// User function Template for Java

class Solution {
    long sumOfSeries(long n) {
        // code here
        long s=0;
        while(n>0)
        {
            s+=n*n*n;
            n-=1;
        }
        return s;
    }
}