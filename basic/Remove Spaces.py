'''
Given a string, remove spaces from it. 

Example 1:

Input:
S = "geeks  for geeks"
Output: geeksforgeeks
Explanation: All the spaces have been 
removed.
Example 2:

Input: 
S = "    g f g"
Output: gfg
Explanation: All the spaces including
the leading ones have been removed.

Your Task:
You don't need to read input or print anything. Your task is to complete the function modify() which takes the string S as input and returns the resultant string by removing all the white spaces from S.


Expected Time Complexity: O(|S|).
Expected Auxiliary Space: O(1).


Constraints:
1<=|S|<=105

 
'''

class Solution:
    def modify(self, s):
        s=s.strip()
        s=s.split()
        return ''.join(s)
