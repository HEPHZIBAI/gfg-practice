'''
Given an integer n, your task is to compute the sum of all natural numbers from 1 to n (inclusive). If n is 0, the sum should be 0.

Examples:

Input: n = 1
Output: 1
Explanation: For n = 1, the sum will be 1.
Input: n = 5
Output: 15
Explanation: For n = 5, sum will be 15. 1 + 2 + 3 + 4 + 5 = 15.
Constraints:
1 <= n <= 104

'''

class Solution {
    public static int seriesSum(int n) {
        return ((n*(n+1))/2);
        
    }
}
