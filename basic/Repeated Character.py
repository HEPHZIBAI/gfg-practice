'''

Given a string consisting of lowercase english alphabets. Find the repeated character present first in the string.

NOTE - If there are no repeating characters return '#'.

Example 1:

Input:
S = "geeksforgeeks"
Output: g
Explanation: g, e, k and s are the repeating
characters. Out of these, g occurs first. 
Example 2:

Input: 
S = "abcde"
Output: -1
Explanation: No repeating character present. (You need to return '#')

Your Task:
You don't need to read input or print anything. Your task is to complete the function firstRep() which takes the string S as input and returns the the first repeating character in the string. In case there's no repeating character present, return '#'.


Expected Time Complexity: O(|S|).
Expected Auxiliary Space: O(1).


Constraints:
1<=|S|<=105

'''

class Solution:
    def firstRep(self, s):
        # code here
        for i in s:
            if s.count(i)>1:
                return i
        return "-1"