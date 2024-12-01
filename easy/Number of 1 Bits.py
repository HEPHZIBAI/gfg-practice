'''
Given a positive integer n. Your task is to return the count of set bits.

Examples:

Input: n = 6
Output: 2
Explanation: Binary representation is '110', so the count of the set bit is 2.
Input: n = 8
Output: 1
Explanation: Binary representation is '1000', so the count of the set bit is 1.
Input: n = 3
Output: 2
Constraints:
1 ≤ n ≤ 109
'''

#User function Template for python3
class Solution:
    def setBits(self, N):
        c=0
        while(N>0):
            c+=(N%2)
            N//=2
        return(c)
