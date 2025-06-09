'''

You are given an integer n. Your task is to reverse the digits, ensuring that the reversed number has no leading zeroes.

Examples:

Input: 200
Output: 2
Explanation: By reversing the digits of number, number will change into 2.
Input : 122
Output: 221
Explanation: By reversing the digits of number, number will change into 221.
Constraints:
1 <= n <= 106

'''

#User function Template for python3

class Solution:
    def reverse_digit(self, n):
        N=str(n)[::-1]
        return int(N)
