'''
Given a string consisting of lowercase English alphabets, reverse only the vowels present in it and print the resulting string.

Examples:

Input: s = "geeksforgeeks"
Output: "geeksforgeeks"
Explanation: The vowels are: e, e, o, e, e. Reverse of these is also e, e, o, e, e.
Input: s = "practice"
Output: "prectica"
Explanation: The vowels are a, i, e. Reverse of these is e, i, a.
Input: s = "bcdfg"
Output: "bcdfg"
Explanation: There are no vowels in s.
Constraints:
1<=|s|<=105
'''

class Solution:
    def modify(self, s):
        k=""
        
        for i in s:
            if i in "aeiou":
                k+=i
                
        k=k[::-1]

        i=0
        j=0
        
        f=""
        
        while i<len(s):
            if s[i] not in "aeiou":
                f+=s[i]
                
            else:
                f+=k[j]
                j+=1
                
            i+=1
                
        
        return f
