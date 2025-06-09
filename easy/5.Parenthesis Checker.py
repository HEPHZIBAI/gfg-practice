'''
Given a string s, composed of different combinations of '(' , ')', '{', '}', '[', ']', verify the validity of the arrangement.
An input string is valid if:

         1. Open brackets must be closed by the same type of brackets.
         2. Open brackets must be closed in the correct order.

Examples :

Input: s = "[{()}]"
Output: true
Explanation: All the brackets are well-formed.
Input: s = "[()()]{}"
Output: true
Explanation: All the brackets are well-formed.
Input: s = "([]"
Output: False
Explanation: The expression is not balanced as there is a missing ')' at the end.
Input: s = "([{]})"
Output: False
Explanation: The expression is not balanced as there is a closing ']' before the closing '}'.
Constraints:
1 ≤ s.size() ≤ 106
s[i] ∈ {'{', '}', '(', ')', '[', ']'}

'''


class Solution:
    def isBalanced(self, s):
        stack=[]
        i=0
        
        while i<len(s):
            if not stack:
                stack.append(s[i])
            else:
                if (s[i]==')' and stack[-1]=='(') or (s[i]=='}' and stack[-1]=='{') or (s[i]==']' and stack[-1]=='['):
                    stack.pop()
                else:
                    stack.append(s[i])
            #print(stack)
            i+=1

        return len(stack)==0