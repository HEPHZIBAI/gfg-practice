'''
Given a string s, the objective is to convert it into integer format without utilizing any built-in functions. Refer the below steps to know about atoi() function.

Cases for atoi() conversion:

Skip any leading whitespaces.
Check for a sign (‘+’ or ‘-‘), default to positive if no sign is present.
Read the integer by ignoring leading zeros until a non-digit character is encountered or end of the string is reached. If no digits are present, return 0.
If the integer is greater than 231 – 1, then return 231 – 1 and if the integer is smaller than -231, then return -231.
Examples:

Input: s = "-123"
Output: -123
Explanation: It is possible to convert -123 into an integer so we returned in the form of an integer
Input: s = "  -"
Output: 0
Explanation: No digits are present, therefore the returned answer is 0.
Input: s = " 1231231231311133"
Output: 2147483647
Explanation: The converted number will be greater than 231 – 1, therefore print 231 – 1 = 2147483647.
Input: s = "-999999999999"
Output: -2147483648
Explanation: The converted number is smaller than -231, therefore print -231 = -2147483648.
Input: s = "  -0012gfg4"
Output: -12
Explanation: Nothing is read after -12 as a non-digit character ‘g’ was encountered.
Constraints:
1 ≤ |s| ≤ 15
'''

class Solution:
    def myAtoi(self, s):
        s=s.strip()
        m=0
        ans=0
        i=0
        
        if s[0]=='-':
            m=1
            i+=1
        
        if s[0]=='+':
            i+=1
            
        while(i<len(s) and s[i]>='0' and s[i]<='9'):
            ans*=10
            ans+=int(s[i])
            i+=1
            #print(ans)
        
        if m==1:
            ans*=-1
        
        if ans>(2**31)-1:
            return (2**31)-1
        elif ans<(-2**31):
            return (2**31)*-1
        
        
            
        return ans