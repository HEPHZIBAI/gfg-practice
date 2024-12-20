'''
Given two strings A and B consisting of lowercase english characters. Find the characters that are not common in the two strings. 

Note :- Return the string in sorted order.

Example 1:

Input:
A = geeksforgeeks
B = geeksquiz
Output: fioqruz
Explanation: 
The characters 'f', 'i', 'o', 'q', 'r', 'u','z' 
are either present in A or B, but not in both.
Example 2:

Input:
A = characters
B = alphabets
Output: bclpr
Explanation: The characters 'b','c','l','p','r' 
are either present in A or B, but not in both.

Your Task:  
You dont need to read input or print anything. Complete the function UncommonChars() which takes strings A and B as input parameters and returns a string that contains all the uncommon characters in sorted order. If no such character exists return "-1".


Expected Time Complexity: O(M+N) where M and N are the sizes of A and B respectively.
Expected Auxiliary Space: O(M+N)  


Constraints:
1<= M,N <= 104
String may contain duplicate characters.
'''

class Solution:
    def UncommonChars(self,A, B):
        #code here
        a=""
        
        for i in A:
            if i not in B:
                a+=i
        for j in B:
            if j not in A:
                a+=j
                
        b=list(set(a))
        b.sort()
        a=""
        for i in b:
            a+=i
        if a=='':
            return "-1"
        return a