/*

Given a string s. The task is to convert characters of string to lowercase.

Example 1:

Input: 
s = "ABCddE"
Output: "abcdde"
Explanation: A, B, C and E are converted to a, b, c and e thus all uppercase characters of the string converted to lowercase letter.
Example 2:

Input: 
s = "LMNOppQQ"
Output: "lmnoppqq"
Explanation: L, M, N, O, and Q are converted to l, m, n, o and q thus all uppercase characters of the string converted to lowercase letter.
Your Task:  
You dont need to read input or print anything. Complete the function toLower() which takes s as input parameter and returns the converted string.

Expected Time Complexity:O(n)
Expected Auxiliary Space: O(1) 

Constraints:
1 <= |s| <= 106
Input only contains lowercase/uppercase English alphabets.



*/

class Solution {
    static String toLower(String s) {
        // code here
        return s.toLowerCase();
    }
}