/*
Given two integers a and b, Your task is to return a list containing their LCM and GCD.

Examples:

Input: a = 5 , b = 10
Output: [10, 5]
Explanation: LCM of 5 and 10 is 10, while their GCD is 5.
Input: a = 14 , b = 8
Output: [56, 2]
Explanation: LCM of 14 and 8 is 56, while their GCD is 2.
Input: a = 1 , b = 1
Output: [1, 1]
Explanation: LCM of 1 and 1 is 1, while their GCD is 1.
Constraints:
1 <= a, b <= 104
*/




class Solution 
{
    static Long gcd(Long A,Long B)
    {
        if(B==0)
            return A;
        else
            return gcd(B,A%B);
    }
    
    static Long[] lcmAndGcd(Long A , Long B) 
    {
        Long[] num=new Long[2];
        
        num[1]=gcd(A,B);
        num[0]=(A*B)/num[1];
        
        return num;
    }
};