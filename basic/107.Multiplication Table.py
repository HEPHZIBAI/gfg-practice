'''
Create the multiplication table from 1 to 10 for a given number n and return the table as an array.

Examples:

Input: n = 9
Output: 9 18 27 36 45 54 63 72 81 90
Input: n = 2
Output: 2 4 6 8 10 12 14 16 18 20
Constraints: 
1 <= N <= 106

'''
#User function Template for python3

class Solution:
    def getTable(self,N):
        a=[]
        for i in range(1,11):
            a.append(i*N)
        return a