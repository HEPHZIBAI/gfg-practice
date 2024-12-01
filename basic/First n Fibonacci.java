/*
Given a number n, return a list containing the first n Fibonacci numbers.

Note: The first two number of the series are 1 and 1.

Examples:

Input: n = 5
Output: [1, 1, 2, 3, 5]
Input: n = 7
Output: [1, 1, 2, 3, 5, 8, 13]
Input: n = 2
Output: [1, 1]
Constraints:
1<= n <=84
*/




//User function Template for Java


class Solution
{
    //Function to return list containing first n fibonacci numbers.
    public static long[] printFibb(int n) 
    {
        long[] num=new long[n];
        long a=0;
        long b=1;
        long c=a+b;
        if(n>=1)
        {
            num[0]=1;
        }
        /*if(n>2)
            num[1]=b;*/
        for(int i=1;i<n;i++)
        {
            num[i]=c;
            a=b;
            b=c;
            c=a+b;
        }
        return num;
    }
}