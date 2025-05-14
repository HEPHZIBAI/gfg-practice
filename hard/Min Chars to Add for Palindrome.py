'''
Given a string s, the task is to find the minimum characters to be added at the front to make the string palindrome.

Note: A palindrome string is a sequence of characters that reads the same forward and backward.

Examples:

Input: s = "abc"
Output: 2
Explanation: Add 'b' and 'c' at front of above string to make it palindrome : "cbabc"
Input: s = "aacecaaaa"
Output: 2
Explanation: Add 2 a's at front of above string to make it palindrome : "aaaacecaaaa"
Constraints:
1 <= s.size() <= 106


'''

class Solution:
    def minChar(self, s):
        extended = s + '$' + s[::-1]
        n = len(extended)
        lps = [0] * n
        length = 0  
        for i in range(1, n):
            while length > 0 and extended[i] != extended[length]:
                length = lps[length - 1]
        
            if extended[i] == extended[length]:
                length += 1
            lps[i] = length
    
        return len(s) - lps[-1]