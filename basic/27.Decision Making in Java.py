'''

Given two integers, n and m. The task is to check the relation between n and m. Return "lesser" if n < m,  "equal" if n == m, and "greater" if n > m.

Examples :

Input: n = 4, m = 8
Output: lesser
Explanation: 4 < 8 so print 'lesser'.
Input: n = 8, m = 8
Output: equal
Explanation: 8 = 8 so print 'equal'.
Input: n = 8, m = 4
Output: greater
Explanation: 8 > 4 so print 'greater'.
Constraints:
-109 <= m , n <= 109

'''


//User function Template for Java
class Solution {
    public static String compareNM(int n, int m) {
        if(n==m)
            return "equal";
        else if(n>m)
            return "greater";
        else
            return "lesser";
        // code here
    }
}