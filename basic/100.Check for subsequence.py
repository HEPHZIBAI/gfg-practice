'''
Given two strings A and B, find if A is a subsequence of B.

Example 1:

Input:
A = AXY 
B = YADXCP
Output: 0 
Explanation: A is not a subsequence of B
as 'Y' appears before 'A'.
 

Example 2:

Input:
A = gksrek
B = geeksforgeeks
Output: 1
Explanation: A is a subsequence of B.
 

Your Task:  
You dont need to read input or print anything. Complete the function isSubSequence() which takes A and B as input parameters and returns a boolean value denoting if A is a subsequence of B or not. 

 

Expected Time Complexity: O(N) where N is length of string B.
Expected Auxiliary Space: O(1)


Constraints:
1<= |A|,|B| <=104

'''


class Solution:
    def isSubSequence(self, A, B):
        ans=""
        x=0
        
        if A in B:
            return 1
        
        while len(B)>0 and x<len(A):
            if A[x] in B:
                f=B.index(A[x])
                B=B[f+1:]
                ans+=A[x]
            else:
                break
            x+=1
                
        return ans==A