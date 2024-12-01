'''
Given two binary strings s1 and s2 consisting of only 0s and 1s. Find the resultant string after adding the two Binary Strings.
Note: The input strings may contain leading zeros but the output string should not have any leading zeros.

Input: s1 = "1101", s2 = "111"
Output: 10100
Explanation:
 1101
+ 111
10100
Input: s1 = "00100", s2 = "010"
Output: 110
Explanation: 
  100
+  10
  110
Constraints:
1 ≤s1.size(), s2.size()≤ 106
'''


class Solution:
	def addBinary(self, s1, s2):
	    '''
	    10 1
	    01 1
	    11 10
	    111 11
	    '''
	    
		while len(s1)<len(s2):
		    s1='0'+s1
		    
		while len(s1)>len(s2):
		    s2='0'+s2
		    
		i=-1
		m=0
		ans=""
		#print(s1)
		#print(s2)
		
		while(abs(i)<=len(s1)):
		    if s1[i]=='0' and s2[i]=='0':
		        if m==1:
		            ans='1'+ans
		            m=0
		        else:
    		        ans='0'+ans
		    elif (s1[i]=='1' and s2[i]=='0') or (s2[i]=='1' and s1[i]=='0'):
		        if m==0:
    		        ans='1'+ans
    		    else:
    		        ans='0'+ans
    		        m=1
		    else:
		        if m!=1:
    		        ans='0'+ans
		            m=1
		        else:
		            ans='1'+ans
		            m=1
		    i-=1
		    #print(ans,m)
        if m==1:
            ans='1'+ans
            
        while ans[0]=='0':
            ans=ans[1:]
		return ans