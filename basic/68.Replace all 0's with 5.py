'''
You are given an integer n. You need to convert all zeroes of n to 5.

Examples:

Input: n = 1004
Output: 1554
Explanation: There are two zeroes in 1004 on replacing all zeroes with 5, the new number will be 1554.
Input: n = 121
Output: 121
Explanation: Since there are no zeroes in 121, the number remains as 121.
Expected Time Complexity: O(k)
Expected Auxillary Space: O(1)
Note:  where k is the number of digits in n

Constraints:
1 <= n <= 104
'''

class Solution:
    def convertFive(self, n):
        # Code here
        a=""
        
        for i in str(n):
            if i=='0':
                a+='5'
            else:
                a+=i
        
        return int(a)
