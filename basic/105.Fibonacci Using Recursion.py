'''
You are given a number n. You need to find nth Fibonacci number.
F(n)=F(n-1)+F(n-2); where F(1)=1 and F(2)=1

Example:

Input: n = 1
Output: 1
Explanation: The first fibonacci number is 1
Input: n = 20
Output: 6765
Explanation: The 20th fibonacci number is 6765
Constraints:
1 <= n <= 20

'''




class Solution:
    def fibonacci(self,n):
        if n<3:
            return 1
            
        a=[1,1]
        while len(a)<n:
            a.append(a[-1]+a[-2])
            
        #print(a)
            
        return a[-1]