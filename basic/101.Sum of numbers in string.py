'''
Given a string str containing alphanumeric characters. The task is to calculate the sum of all the numbers present in the string.

Examples:

Input: s = "1abc23"
Output: 24
Explanation: 1 and 23 are numbers in the string which is added to get the sum as 24.
Input: s = "geeks4geeks"
Output: 4
Explanation: 4 is the only number, so the sum is 4.
Constraints:
1 <= length of the string <= 105
The sum of Numbers <= 105

'''


class Solution:
    def findSum(self, s):
        i=0
        ans=0
        
        while len(s)>i:
            a=""
            while(len(s)>i and s[i]>='0' and s[i]<='9'):
                a+=s[i]
                i+=1
              
            if a!='':   
                a=int(a)
            else:
                a=0
            ans+=a
            
            while(len(s)>i and s[i]>='a' and s[i]<='z'):
                i+=1
            

        return ans