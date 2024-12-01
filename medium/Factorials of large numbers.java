/*
Given an integer n, find its factorial. Return a list of integers denoting the digits that make up the factorial of n.

Examples:

Input: n = 5
Output: [1, 2, 0]
Explanation: 5! = 1*2*3*4*5 = 120
Input: n = 10
Output: [3, 6, 2, 8, 8, 0, 0]
Explanation: 10! = 1*2*3*4*5*6*7*8*9*10 = 3628800
Input: n = 1
Output: [3]
Explanation: 1! = 1 
Constraints:
1 ≤ n ≤ 103
*/

// User function Template for Java
import java.math.BigInteger;
import java.util.ArrayList;
class Solution 
{
    static ArrayList<Integer> factorial(int N) 
    {
        BigInteger factorial = BigInteger.ONE;
        
        for (int i = 2; i <= N; i++) 
        {
            factorial = factorial.multiply(BigInteger.valueOf(i));
        }
        
        String factorialStr = factorial.toString();
        ArrayList<Integer> result = new ArrayList<>();
        
        for (char c : factorialStr.toCharArray()) 
        {
            result.add(Character.getNumericValue(c));
        }
        
        return result;
    }
}