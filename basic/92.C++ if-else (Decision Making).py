'''
Given an integer N. Your task is to check if the integer is greater than, less than or equal to 5.
If the integer is greater than 5, then print "Greater than 5" (without quotes).
If the integer is less than 5, then print "Less than 5".
If the integer is equal to 5, then print "Equal to 5".

Note:- Do not print the next line after the result.

Example 1:

Input:
N = 8
Output:
Greater than 5
 

Example 2:

Input:
N = 4
Output:
Less than 5
 

Your Task:

You don't need to read input or print anything. Your task is to complete the function compareFive() which takes the number N and returns "Greater than 5" if the integer is greater than 5 or "Less than 5" if the integer is less than 5 otherwise print "Equal to 5" if the integer equals to 5.

Expected Time Complexity: O(1)
Expected Auxiliary Space: O(1)

 

Constraints:
1 <= N <= 100000

'''


#User function Template for python3
class Solution:
    def compareFive (ob,N):
        if N>5:
            return("Greater than 5")
        elif N==5:
            return("Equal to 5")
        else:
            return("Less than 5")