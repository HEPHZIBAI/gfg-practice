'''
You are given two integer numbers, the base a and the index b. You have to find the last digit of ab.

Examples:

Input: a = "3", b = "10"
Output: 9
Explanation: 310 = 59049. Last digit is 9.
Input: a = "6", b = "2"
Output: 6
Explanation: 62 = 36. Last digit is 6.
Your Task:
You don't need to read input or print anything. Your task is to complete the function getLastDigit() which takes two strings a,b as parameters and returns an integer denoting the last digit of ab.

Expected Time Complexity: O(|b|)
Expected Auxiliary Space: O(1)

Constraints:
1 <= |a|,|b| <= 1000

Note: |a| = length of a and |b| = length of b. There will not be any test cases such that ab is undefined.
'''

#User function Template for python3

class Solution:
    def getLastDigit(self, a, b):
        a = int(a)
        b = int(b)
        if b == 0:
            return 1

        if a == 0:
            return 0
    
        if b % 4 == 0:
            res = 4
        else:
            res = b % 4
        
        num = pow(a, res)
    

        return num % 10



# This code is contributed by Naimish14.

