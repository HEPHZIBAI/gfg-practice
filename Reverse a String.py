'''
You are given a string s. You need to reverse the string.

Examples:

Input: s = "Geeks"
Output: "skeeG"
Input: s = "for"
Output: "rof"
Expected Time Complexity: O(|s|)
Expected Auxiliary Space: O(1)

Constraints:
1 <= |s| <= 104
'''

class Solution:
     def reverseString(self, s: str) -> str:
        #your code here
        return s[::-1]
